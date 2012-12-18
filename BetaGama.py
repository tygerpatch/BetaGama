# Derived from László Németh's Lightproof grammar checker
# https://launchpad.net/lightproof
# 2009 (c) László Németh (nemeth at OO.o), license: GNU LGPL

import uno
import unohelper
import sys
import re

from com.sun.star.linguistic2 import XProofreader
from com.sun.star.linguistic2 import XSupportedLocales
from com.sun.star.linguistic2 import ProofreadingResult
from com.sun.star.linguistic2 import SingleProofreadingError
from com.sun.star.lang import XServiceInfo
from com.sun.star.lang import XServiceName
from com.sun.star.lang import XServiceDisplayName
from com.sun.star.lang import Locale
from com.sun.star.text.TextMarkupType import PROOFREADING

ignore = {}

import grammar_rule
import graviax
import richard_nordquist

rules = []

rules.extend( graviax.rules )
rules.extend( richard_nordquist.rules )

def create_proofreading_error(starting_position_of_text, match, rule):
  proofreading_error = uno.createUnoStruct( "com.sun.star.linguistic2.SingleProofreadingError" )                      
  proofreading_error.nErrorStart = starting_position_of_text + match.start()      
  proofreading_error.nErrorLength = match.end() - match.start()            
  proofreading_error.nErrorType = PROOFREADING
            
  #proofreading_error.aSuggestions = rule.suggestion,
  proofreading_error.aSuggestions = re.sub(rule.pattern, rule.suggestion, match.group()),
  # TODO: replace with object method
              
  proofreading_error.aShortComment = rule.short_comment                        
  
  #proofreading_error.aFullComment = rule.full_comment           
  proofreading_error.aFullComment = re.sub(rule.pattern, rule.full_comment, match.group())
  # TODO: replace with object method
  
  proofreading_error.aProperties = ()      
  return proofreading_error

def proofread( text, starting_position_of_text ):
  global rules
  proofreading_errors = []
  
  for rule in rules:    
    for match in rule.pattern.finditer(text):
      if not rule.exceptions:
        proofreading_errors.append( create_proofreading_error(starting_position_of_text, match, rule) )
      else:
        for key, value in rule.exceptions.iteritems():
          if match.group(key) not in value:
            proofreading_errors.append( create_proofreading_error(starting_position_of_text, match, rule) )

  return tuple(proofreading_errors)

# based on LightProof's LightProof class
class BetaGama( unohelper.Base, XProofreader, XServiceInfo, XServiceName, XServiceDisplayName, XSupportedLocales):

  def __init__( self, ctx, *args ):
    self.ServiceName = "com.sun.star.linguistic2.Proofreader"
    self.ImplementationName = "org.openoffice.comp.pyuno.BetaGama.en_US"
    self.SupportedServiceNames = self.ServiceName, 
    self.locales = Locale('en', 'US', ''), 
  
  # *** XServiceName
  
  def getServiceName(self):
    return self.ImplementationName
  
  # *** XServiceInfo
  
  def getImplementationName (self):
    return self.ImplementationName
  
  def supportsService(self, ServiceName):
    return (ServiceName in self.SupportedServiceNames)
  
  def getSupportedServiceNames (self):
    return self.SupportedServiceNames
  
  # *** XSupportedLocales
  
  def hasLocale(self, aLocale):
    
    if aLocale in self.locales:
      return True
      
    for i in self.locales:
      if i.Country == "" and aLocale.Language == i.Language:
        return True
        
    return False
  
  def getLocales(self):
    return self.locales
  
  # *** XProofreader 
  def isSpellChecker(self):
    return False

  def doProofreading(self, document_identifier, text, locale, starting_position_of_text, probable_ending_position_of_text, properties):
    proofreading_result = uno.createUnoStruct( "com.sun.star.linguistic2.ProofreadingResult" )
    proofreading_result.aDocumentIdentifier = document_identifier
    proofreading_result.aText = text
    proofreading_result.aLocale = locale
    proofreading_result.nStartOfSentencePosition = starting_position_of_text
    proofreading_result.nStartOfNextSentencePosition = probable_ending_position_of_text
  
    try:
      proofreading_result.aErrors = proofread( text, starting_position_of_text )
    except:
      proofreading_result.aErrors = ()
  
    proofreading_result.aProperties = ()
    proofreading_result.xProofreader = self
  
    return proofreading_result
  
  def ignoreRule(self, rule_id, locale):
    global ignore   
    ignore[rule_id] = 1
  
  def resetIgnoreRules(self):
    global ignore
    ignore = {}
  
  # *** XServiceDisplayName
  
  def getServiceDisplayName(self, aLocale):
    return "Beta Gama"

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( BetaGama, "org.openoffice.comp.pyuno.BetaGama.en_US", ("com.sun.star.linguistic2.Proofreader",),)


