
class String:
    def get_str(self):
        self.content = str(input())

    def print_str(self):
        print(self.content)

x = String()
print("Enter String:")
x.get_str()
x.print_str()
