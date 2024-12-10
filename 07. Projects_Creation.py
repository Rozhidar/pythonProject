architect_name = input()
projects_count = int(input())

hours_to_finish_one_project = 3

time_for_projects = projects_count * hours_to_finish_one_project

print(f"The architect {architect_name} will need \
{time_for_projects} hours to complete {projects_count} project/s.")