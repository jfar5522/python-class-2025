def main():
    print("Hello from main")
    class MyException(BaseException):
        def __init__(self, message, *args):
            super().__init__(*args)
            self.message = message

    class FiveException(MyException):
        pass

    class SevenException(MyException):
        pass

    class TenException(MyException):
        pass

    try:
        for i in range(10):
            print(i)
            if i == 5:
                raise FiveException(f"A {i} was discovered in the soup!")
            if i == 7:
                raise SevenException(f"A {i} was discovered in the soup!")
            if i == 10:
                raise TenException(f"A {i} was discovered in the soup!")
        pass
    except SevenException as e:
        print(e.message)
    except FiveException as e:
        print(e.message)
    except TenException as e:
        print(e.message)
    else:
        print("Ze operation vas a success!")
    finally:
        print("We've made it to the end finally.")
        
if __name__ == "__main__":
    main()