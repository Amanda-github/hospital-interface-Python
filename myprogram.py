# the file/script name automatically becomes the module name
# from hellomodule import say_hello

# say_hello('english')
# say_hello('chinese')
# say_hello('spanish')
# say_hello('italian')
# say_hello('french')
# say_hello('hindi')
# say_hello('thai')

# from my_package import mymainscript
# from my_package.sub_package import mysubscript

# mymainscript.languages_available()
# mysubscript.say_hello("French")

# directly importing function from a package
from my_package.mymainscript import languages_available  # as something
from my_package.sub_package import mysubscript

languages_available()
mysubscript.say_hello("French")

# something.language_available ......
