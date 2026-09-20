from functions.get_files_info import get_files_info

def print_result(test_function, working_directory , directory):
    display_dir = "current" if directory == "." else directory 
    print(f"Result for {display_dir} directory:\n{test_function(working_directory, directory)}")




print_result(get_files_info, "calculator", ".")
print_result(get_files_info, "calculator", "pkg")
print_result(get_files_info, "calculator", "/bin")
print_result(get_files_info, "calculator", "../")




#former test calls
#print(get_files_info("calculator", ".")) #working_directory, directory
#print(get_files_info("calculator", "/bin"))
#print(get_files_info("calculator", "../"))
#print(get_files_info("calculator", "main.py"))

