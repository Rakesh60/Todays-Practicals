def student(*args, **kwargs):
    def display_args():
        print("Positional arguments:")
        for arg in args:
            print(arg)
        print("Keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key} = {value}")
    student.display_args = display_args
    return student
 