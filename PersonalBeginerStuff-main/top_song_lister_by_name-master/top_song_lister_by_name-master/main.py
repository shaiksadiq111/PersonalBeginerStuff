import tkinter
import requests
import bs4
import smtplib

bg_color = "#f2a154"
my_email = "bada.heavy.driver@gmail.com"
my_password = "sytjyk-vurjic-8Doxga"

style = ("Courier", 25, "bold")
display1 = tkinter.Tk()
display1.title("Top songs teller")
display1.configure(bg=bg_color, width=650, height=400)

label1 = tkinter.Label()
label1.config(text="Enter the date you want top songs for:", bg=bg_color, font=style)
label1.place(x=20, y=60)

day_label = tkinter.Label()
day_label.config(bg=bg_color, text="Day", font=("Arial", 20))
day_label.place(x=80, y=150)

day_entry = tkinter.Entry()
day_entry.configure(width=6)
day_entry.focus()
day_entry.place(x=80, y=200)

month_label = tkinter.Label()
month_label.config(bg=bg_color, text="Month", font=("Arial", 20))
month_label.place(x=270, y=150)

month_entry = tkinter.Entry()
month_entry.configure(width=6)
month_entry.place(x=270, y=200)

year_label = tkinter.Label()
year_label.config(bg=bg_color, text="Year", font=("Arial", 20))
year_label.place(x=450, y=150)

year_entry = tkinter.Entry()
year_entry.configure(width=6)
year_entry.place(x=450, y=200)


def done_function():
    global date
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    if month < 10:
        month = f"0{month}"
    if day < 10:
        day = f"0{day}"
    date = f"{year}-{month}-{day}"
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    request = requests.get(url=url)
    request.raise_for_status()
    html_ = request.content
    html = bs4.BeautifulSoup(html_, "html.parser")
    class_tag = "chart-element__information__song text--truncate color--primary"
    all_songs = html.find_all("span", class_=class_tag)
    songs = [song.string for song in all_songs]
    display1.destroy()

    def create_display2():
        display2 = tkinter.Tk()
        display2.title("Top songs Teller")
        display2.configure(bg=bg_color, width=1000, height=600)

        mail_info_label = tkinter.Label(display2)
        mail_info_label.configure(text="If you want to get your list mailed enter your mail id below: ", bg=bg_color,
                                  font=style)
        mail_info_label.place(x=30, y=60)

        mail_entry = tkinter.Entry(display2)
        mail_entry.configure(width=30)
        mail_entry.focus()
        mail_entry.place(x=280, y=130)

        def send_mail_function():
            message = f"Subject: Your list for top songs of {date}\n\n{songs}"
            email_id = mail_entry.get()
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=email_id, msg=message)

        send_mail_button = tkinter.Button(display2)
        send_mail_button.configure(text="Send Mail", font=style, command=send_mail_function)
        send_mail_button.place(x=340, y=190)

    create_display2()


done_button = tkinter.Button()
done_button.configure(text="Done", font=style, command=done_function)
done_button.place(x=270, y=290)

display1.mainloop()
