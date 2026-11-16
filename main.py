#  - آلة حاسبة ذكية
print("="*30)
print("  أهلا بيك في حاسبتي الذكية 👋")
print("="*30)

name = input("اكتب اسمك: ")
print(f"\nمرحب بيك يا {name}!\n")

while True:
    print("\nاختار العملية:")
    print("1 - جمع +")
    print("2 - طرح -")
    print("3 - ضرب *")
    print("4 - قسمة /")
    print("5 - خروج")

    choice = input("رقم العملية (1-5): ")

    if choice == "5":
        print(f"\nشكرا يا {name}، شرفتنا! 🙏")
        break

    if choice not in ["1","2","3","4"]:
        print("اختيار غلط، حاول تاني")
        continue

    try:
        num1 = float(input("الرقم الأول: "))
        num2 = float(input("الرقم التاني: "))

        if choice == "1":
            result = num1 + num2
            print(f"النتيجة: {num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"النتيجة: {num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"النتيجة: {num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("ما ممكن نقسم على صفر!")
            else:
                result = num1 / num2
                print(f"النتيجة: {num1} / {num2} = {result}")
    except:
        print("اكتب ارقام بس يا معلم!")