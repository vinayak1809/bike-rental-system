
class main:

    available_bikes = {
        "kawasaki": 8, "ninja": 3, "unicorn": 5, "pulsur": 7
    }

    print("\navailable bikes ::\n")

    for bikes, quantity_of_bikes in (available_bikes.items()):
        print(bikes + ": " + str(quantity_of_bikes))

    rupee = u'\u20B9'
    cost = {"hour": rupee+"400", "day": rupee+"1500", "weak": rupee+"4500"}

    print("\ncost of bikes :: \n")
    for time_span, money in (cost.items()):
        print(time_span + ": " + str(money))

    print(" ")

    done = False

    def bymore():
        print()
        ask = input("do u want to rent more bikes(Y/N) : ").upper()
        if ask == "Y" or "YES":
            main.done = False
        else:
            exit()


class hour_day_week:

    rupee = u'\u20B9'

    def hourly_basis():

        for ask in main.available_bikes.keys():

            if ask_bike == ask:
                hour_price = 500

                payment_tobe_paid = hour_price * num_of_bikes_want
                if num_of_bikes_want > 3:
                    payment_tobe_paid = payment_tobe_paid * (30/100)

                print("payment to be paid is :: " +
                      hour_day_week.rupee+str(+payment_tobe_paid))
                payment = int(input("payment :: "))

                if payment == payment_tobe_paid:

                    main.available_bikes[ask] = main.available_bikes[ask] - \
                        num_of_bikes_want

                    print("Thankyou! Have a great day ")
                    main.bymore()

    def day_basis():
        for ask in main.available_bikes.keys():
            if ask_bike == ask:
                day_price = 1500

                payment_tobe_paid = day_price * num_of_bikes_want
                if num_of_bikes_want > 3:
                    payment_tobe_paid = payment_tobe_paid * (30/100)

                print("payment to be paid is :: " +
                      hour_day_week.rupee+str(payment_tobe_paid))
                payment = int(input("payment :: "))

                if payment == payment_tobe_paid:
                    main.available_bikes[ask] = main.available_bikes[ask] - \
                        num_of_bikes_want

                    print("Thankyou! Have a great day ")
                    main.bymore()

    def weekly_basis():
        for ask in main.available_bikes.keys():
            if ask_bike == ask:
                week_price = 4500

                payment_tobe_paid = week_price * num_of_bikes_want
                if num_of_bikes_want > 3:
                    payment_tobe_paid = payment_tobe_paid * (30/100)

                print("payment to be paid is :: " +
                      hour_day_week.rupee+str(payment_tobe_paid))
                payment = int(input("payment :: "))

                if payment == payment_tobe_paid:
                    main.available_bikes[ask] = main.available_bikes[ask] - \
                        num_of_bikes_want

                    main.bymore()


def check(time_limit):
    obj = hour_day_week

    if time_limit == "hour":
        obj.hourly_basis()

    elif time_limit == "day":
        obj.day_basis()

    elif time_limit == "week":
        obj.weekly_basis()

    else:
        print("this bike is not available")


while not main.done:
    done_ask = False
    return_rent = input(
        "do u want to return or rent the bike (return/rent) :: ").lower()

    if return_rent == "rent":
        while not done_ask:
            ask_bike = input("which bike do u want :: ").lower()

            if ask_bike in main.available_bikes.keys():
                num_of_bikes_want = int(
                    input("How many bikes would you like to rent :: "))

                if num_of_bikes_want > main.available_bikes[ask_bike]:
                    print("this much bikes are not available ")
                else:
                    time_limit = input("time you need :: ").lower()
                    check(time_limit)

            else:
                print("retype the bike name :")
                done_ask = False

    elif return_rent == "return":
        bike_return = input("bike name to be returned :: ").lower()
        num_of_bikes_to_be_return = int(
            input("num of bikes to be returned : "))

        for bikes in main.available_bikes.keys():
            if bike_return == bikes:
                main.available_bikes[bikes] = main.available_bikes[bikes] + \
                    num_of_bikes_to_be_return

                print("\navailable bikes ::")

                for bikes, quatity_of_bikes in (main.available_bikes.items()):
                    print(bikes + ": " + str(quatity_of_bikes))

        print("\nthankyou :) ")
        exit()
    else:
        print("type again return/rent")
        main.done = False
