import sys, os, time, datetime
import docx                                                                                            
from   docx.shared          import RGBColor, Pt                                                      
from   docx.enum.text       import WD_ALIGN_PARAGRAPH
from   colorama             import *
from   art                  import *
################################################################################################################# A  J #####################################################################################################################
###VARS
# path  var
here       = os.getcwd()
# clear var (used print(clear) to clear space)
clear      = "\033[2J\033[1;1f"
# time variables
today      = datetime.date.today().strftime("%d-%m-%Y")
now        = str(datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y"))

# defining AJ function
def AJ():
       newentry = ""
       print(clear)
       print("\n"*10)
       print("""






                                                                                                                  
                                                                                                         """+Fore.LIGHTRED_EX+"""   ##############      """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""    ##################  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""  #              #     """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+""" #                #    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""####################   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""####################   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                     #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""   #                 #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""    #                #  """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""     #              #   """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""      #            #    """+Style.RESET_ALL+"""
                                                                                                         """+Fore.LIGHTRED_EX+"""#                  #  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""#       ############     #"""+Style.RESET_ALL+Style.BRIGHT+"""                                                         """+Fore.LIGHTBLACK_EX+"""["""+Fore.LIGHTRED_EX+"""A"""+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""utomated """+Fore.LIGHTRED_EX+"""J"""+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""ournal] ("""+Fore.LIGHTRED_EX+"""v7.0"""+Style.RESET_ALL+Fore.LIGHTBLACK_EX+""")"""+Style.RESET_ALL+"""
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|""")
       print("")
       print(now+Style.RESET_ALL)
       newentry = input("")
       