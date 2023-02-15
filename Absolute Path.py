#Given a file path with folder names, '..' (Parent directory), and '.' (Current directory), return the shortest possible file path (Eliminate all the '..' and '.').



def shortest_path(file_path):

    components = file_path.split('/')

    stack = []

    for component in components:

        if component == '..':

            if stack != "":

                stack.pop(-1)

        elif component != '.' and component != '':

            stack.append(component)

    return '/' + '/'.join(stack)



print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))

# Output: /Users/Joma

