import tkinter
import json
import smtplib
import time

bg_color = "#d8c292"
my_email = "bada.heavy.driver@gmail.com"
my_password = "sytjyk-vurjic-8Doxga"
style = ("Courier", 20, "bold")

display = tkinter.Tk()
display.title("Email Sender")
display.configure(width=1000, height=700, bg=bg_color)

label1 = tkinter.Label()
label1.configure(text="Enter the name of list you want to send mail to: ", bg=bg_color, font=style)
label1.place(x=10, y=500)

list_input = tkinter.Entry()
list_input.configure(font=style)
list_input.place(x=650, y=500)

label2 = tkinter.Label()
label2.configure(text="Click the button to generate a new list >>", font=style, bg=bg_color)
label2.place(x=10, y=570)

subject_label = tkinter.Label()
subject_label.configure(font=style, bg=bg_color, text="Enter subject of mail:")
subject_label.place(x=20, y=25)

subject_entry = tkinter.Entry()
subject_entry.configure(font=style)
subject_entry.place(x=400, y=30)
subject_entry.focus()

body_label = tkinter.Label()
body_label.configure(text="Enter body of the mail", font=style, bg=bg_color)
body_label.place(x=20, y=100)

body_text = tkinter.Text()
body_text.configure(width=80, height=10)
body_text.place(x=330, y=100)


def pop_list_name():
    list_window = tkinter.Tk()
    list_window.configure(width=350, height=180, bg=bg_color)
    list_window.title("List Name")
    label_list_name = tkinter.Label(list_window)
    label_list_name.configure(bg=bg_color, text="Enter below the name of list to create:")
    label_list_name.place(x=30, y=30)
    list_name_entry = tkinter.Entry(list_window)
    list_name_entry.configure(font=style)
    list_name_entry.place(x=30, y=80)
    list_name_entry.focus()

    def done_function():
        global new_list_name
        new_list_name = list_name_entry.get()
        list_window.destroy()
        email_entry_for_list()

    done_button = tkinter.Button(list_window)
    done_button.configure(text="DONE", font=style, command=done_function)
    done_button.place(x=100, y=140)


def email_entry_for_list():
    new_list = []
    generate_window = tkinter.Tk()
    generate_window.title("Enter email addresses")
    generate_window.configure(bg=bg_color, width=880, height=300)
    label_instruction = tkinter.Label(generate_window)
    label_instruction.configure(text="Enter email addresses and keep on pressing save after each address", bg=bg_color,
                                font=style)
    label_instruction.place(x=20, y=30)
    new_mail = tkinter.Entry(generate_window)
    new_mail.configure(font=style)
    new_mail.place(x=170, y=100)
    new_mail.focus()

    def save():
        new_address = new_mail.get()
        new_list.append(new_address)
        new_mail.delete(0, "end")

    save_button = tkinter.Button(generate_window)
    save_button.configure(text="Save", font=style, command=save)
    save_button.place(x=250, y=150)

    def complete_function():
        generate_window.destroy()
        with open("data.json") as file:
            data = json.load(file)
            data[new_list_name] = new_list
        with open("data.json", "w") as file_:
            json.dump(data, file_, indent=4)

    complete_button = tkinter.Button(generate_window)
    complete_button.configure(text="complete", font=style, command=complete_function)
    complete_button.place(x=650, y=230)


def generate():
    pop_list_name()


def Send():
    list_name = list_input.get()
    mail_subject = subject_entry.get()
    mail_body = body_text.get("1.0", "end")

    with open("data.json", 'r') as file:
        data = json.load(file)
        req_list = data[list_name]
        mail_text = f"Subject:{mail_subject} \n\n{mail_body}"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        counter = 0
        for reciever_mail in req_list:
            connection.sendmail(from_addr=my_email, to_addrs=reciever_mail, msg=mail_text)
            counter += 1
            if counter == 65:
                print("waiting")
                connection.close()
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=my_email, password=my_password)
            elif counter == 130:
                print("waiting2")
                connection.close()
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=my_email, password=my_password)
            elif counter == 190:
                print("waiting3")
                connection.close()
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=my_email, password=my_password)

        print("Mail sent to the list")


def Send_mail():
    email_recipient = address_entry.get()
    subject_mail = subject_entry.get()
    body_mail = body_text.get("1.0", "end")
    mail_text = f"Subject:{subject_mail}\n\n{body_mail}"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=email_recipient, msg=mail_text)
    connection.close()
    print("a single mail sent ")


generate_button = tkinter.Button()
generate_button.configure(text="Generate", font=style, command=generate)
generate_button.place(x=600, y=570)

send_button = tkinter.Button()
send_button.configure(text="Send", font=style, command=Send)
send_button.place(x=400, y=640)

label_or = tkinter.Label()
label_or.configure(text="OR", font=("Arial", 40, "bold"), bg=bg_color)
label_or.place(x=400, y=450)

label_address = tkinter.Label()
label_address.configure(text="Enter the email address whom you want to send: ", font=style, bg=bg_color)
label_address.place(x=20, y=330)

address_entry = tkinter.Entry()
address_entry.configure(font=style)
address_entry.place(x=600, y=330)

send_mail_button = tkinter.Button()
send_mail_button.configure(text="Send Mail", font=style, command=Send_mail)
send_mail_button.place(x=400, y=410)

display.mainloop()
