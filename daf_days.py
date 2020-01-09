import datetime
from zmanim.limudim.calculators.daf_yomi_bavli import DafYomiBavli
import tkinter as tk

# build executable with pyinstaller --onefile --noconsole .\daf_days.py  
root= tk.Tk()
root.title("Daf Yomi")
canvas = tk.Canvas(root, width = 500, height = 500)
canvas.pack()
text = tk.Text(canvas, wrap=tk.WORD)
text.pack()

today = datetime.date.today()
limud = DafYomiBavli().limud(today)
current_cycle_end_date = limud.cycle_end_date()
current_cycle_start_date = limud.cycle_start_date()
diff = current_cycle_end_date - today
start_diff = today - current_cycle_start_date.gregorian_date
text.insert(tk.END, "Today's Daf Is: " + limud.description(), )
text.insert(tk.END, "\n")
text.insert(tk.END,"The current Daf Yomi cycle started on: " + str(current_cycle_start_date.jewish_day) +
      " " +
      current_cycle_start_date.jewish_month_name() +
      " " + str(current_cycle_start_date.jewish_year)
      + " (" + current_cycle_start_date.gregorian_date.strftime('%B %d, %Y') + ")")
text.insert(tk.END, "\n")
text.insert(tk.END,"The current Daf Yomi cycle will end on: " + str(current_cycle_end_date.jewish_day) +
      " " + current_cycle_end_date.jewish_month_name() + " " + str(current_cycle_end_date.jewish_year)
      + " (" + current_cycle_end_date.gregorian_date.strftime('%B %d, %Y') + ")")
text.insert(tk.END, "\n")
text.insert(tk.END,str(start_diff.days) + " days have passed since the start of the Daf Yomi cycle.")
text.insert(tk.END, "\n")
text.insert(tk.END,"There are " + str(diff.days) +
      " days left until the end of the Daf Yomi cycle.")
percentage = start_diff.days/2711 * 100
text.insert(tk.END, "\n")
text.insert(tk.END,str(percentage) + "% of the current Daf Yomi cycle has been completed.")

root.mainloop()