class GreetingGenerator:
    
    __greeting = "hello world!"
    
    def get_greeting(self):
        return self.__greeting
    
    def do_greet(self):
        print(self.get_greeting())
        

def main():
    gg = GreetingGenerator()
    gg.do_greet();

if __name__ == '__main__':
    main()
