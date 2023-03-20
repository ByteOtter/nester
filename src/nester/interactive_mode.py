"""
Interactive Mode implementation halted until after initial release!
"""

# def interactive_mode():
#     print(
#         "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
#     )
#     print("No arguments given. Launching interactive mode ...")

#     userInput = ""

#     while True:
#         userInput = input(
#             "Which operation shall be performed?(create, validate, clean)\n"
#         )
#         if userInput not in ALLOWED_OPERATIONS:
#             print("ERROR: Please enter a valid operation!(create, validate, clean)\n")
#             continue
#         else:
#             OPERATION = userInput
#             print("Selected operation: " + OPERATION)
#             break

#     while True:
#         userInput = input(
#             "What language would you like to generate the structure for?\n(py, cpp, c, cs, rb)\n"
#         )
#         if userInput not in LANGUAGES:
#             print("ERROR: Please enter a supported language!\n(py, cpp, c, cs, rb)\n")
#             continue
#         else:
#             LANGUAGE = userInput
#             print("Selected language: " + LANGUAGE)
#             break
