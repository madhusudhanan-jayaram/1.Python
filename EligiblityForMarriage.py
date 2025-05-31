#create a function that tells eligility of marriage for male and female according to their age limit like 21 for male and 18 for female
class EligiblityForMarriage():
    def eligileForMarriage():
        gender = input("Enter your Gender: ")
        age = int(input("Enter your Age: "))
        upper_gender = gender.upper().strip()
        print (f"Your gender: {upper_gender}")
        print (f"Your age: {age}")
        if (upper_gender =='MALE'):
            if (age >= 18):
                print("ELIGIBLE FOR MARRIAGE")
            else:
                print("NOT ELIGIBLE FOR MARRIAGE")
        elif(upper_gender =='FEMALE'):
            if (age >= 21):
                print("ELIGIBLE FOR MARRIAGE")
            else:
                print("NOT ELIGIBLE FOR MARRIAGE")
        else:
            print ("you've entered the unacceptable gender")