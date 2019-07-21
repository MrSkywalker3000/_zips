import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser


def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
		function4,
		function5,
		function6,
		function7,
		function8,
		function9,
		function10,
		function11,
		function12,
		function13,
		function14,
		function15,
		function16,
		function17,
		function18,
		function19,
		function20,
		function21
        )
        
    call = dialog.select('[COLORfffefe33][B][I]iSw!tch Streams[/I][/B][/COLOR][COLORffff0066] .[/COLOR]', [
	'[COLORfffefe33]* [/COLOR] [COLOR white]Packages & Prices[/COLOR]',
	'[COLORfffefe33]* [/COLOR] [COLOR white]Request 48hs Trial[/COLOR]',
	'[COLORfffefe33]* [/COLOR] [COLOR white]Channel List[/COLOR]',
    '[COLORfffefe33]* [/COLOR] [COLOR white]Service in action[/COLOR]',
    '[COLORfffefe33]* [/COLOR] [COLOR white]Website[/COLOR]',
	'[COLORfffefe33]* [/COLOR] [COLORffff0066][B][I]iSw!tch Streams[/I][/B][/COLOR] [COLOR white]APK[/COLOR] [COLORfffefe33]Android Devices Only[/COLOR]',
    '[COLORfffefe33]* [/COLOR] [COLORfffefe33]APK offers multiscreen - It is truly spectacular![/COLOR]',])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-21]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()

def function1():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://iswitchlive.mytvpro.org/home/pricing' ) )
    else:
        opensite = webbrowser . open('https://iswitchlive.mytvpro.org/home/pricing')

def function2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://iswitchlive.mytvpro.org/home/trial' ) )
    else:
        opensite = webbrowser . open('https://iswitchlive.mytvpro.org/home/trial')
        
def function3():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://iswitchlive.mytvpro.org/home/channel' ) )
    else:
        opensite = webbrowser . open('https://iswitchlive.mytvpro.org/home/channel')
		
def function4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://youtu.be/9sQaTSCwnZM' ) )
    else:
        opensite = webbrowser . open('https://youtu.be/9sQaTSCwnZM')		
		
def function5():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://iswitchlive.mytvpro.org' ) )
    else:
        opensite = webbrowser . open('https://iswitchlive.mytvpro.org')
		
def function6():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://iswitchstreams.com/apk/iSwitchTVPRO.apk' ) )
    else:
        opensite = webbrowser . open('http://iswitchstreams.com/apk/iSwitchTVPRO.apk')	
				
def function7():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://iswitchstreams.com/apk/iSwitchTVPRO.apk' ) )
    else:
        opensite = webbrowser . open('http://iswitchstreams.com/apk/iSwitchTVPRO.apk')

def function8():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')

def function9():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')

def function10():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')

def function11():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')

def function12():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')		
		
 
def function13(): 0	

def function14():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('http://getnow.hypersonic-tv.com/home/freetrial')	

def function15():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('http://getnow.hypersonic-tv.com/home/pricing')	

def function16():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')

def function17():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')

def function18():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')

def function19():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')	
		
def function20(): 0	

def function21():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( '' ) )
    else:
        opensite = webbrowser . open('')		
 
menuoptions()
