try:
    1/0
except Exception as e:
    print(type(e).__name__, "-", e)

# # potential code before try catch
#
# try:
# # code to try to execute
# except ZeroDivisionError:
# # code to execute if there is a ZeroDivisionError
# except NameError:
# # code to execute if there is a NameError
# except:
# # code to execute if ther is any exception
# else:
# # code to execute if there is no exception
# finally:
# # code to execute at the end of the try except no matter what
#
# # code that will execute if there is no exception or a one that we are handling