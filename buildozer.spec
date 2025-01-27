[app]
# (str) Title of your application
title = Social Media Limit App
# (str) Package name
package.name = socialmedialimit
# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (list) Application requirements
# Comma separated e.g. requirements = sqlite3,kivy,plyer
requirements = kivy,plyer

# (list) Application icons
icon.filename = %(source.dir)s/resources/app_icon.png

[android]
# (str) Android API to use
android.api = 29

# (str) Android NDK version to use
android.ndk = 21b

# (str) Android package
android.package = org.example.socialmedialimit

# (list) Application permissions
# Example: android.permissions = INTERNET,ACCESS_FINE_LOCATION
android.permissions = ACCESS_FINE_LOCATION,PACKAGE_USAGE_STATS

# (bool) Whether to copy library dependencies to the APK
android.copy_libs = True
