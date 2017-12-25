while True:
    try:
        num = int(input("Enter a number: \n"))
        print(18/num)
        break
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Number can't be zero")
    except:
        break
    finally:
        print("Loop complete")
