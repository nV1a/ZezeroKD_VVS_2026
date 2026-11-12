import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('Barca tracker')
root.geometry('800x650')

def update_stats():
    wins = 0
    draws = 0
    losses = 0
    for m in matches:
        if m['barca'] > m['opp']:
            wins += 1
        elif m['barca'] == m['opp']:
            draws += 1
        else:
            losses += 1
    stats_label.config(text=f'W: {wins}   D: {draws}   L: {losses}')

def delete_match():
    selected = matches_list.curselection()
    if not selected:
        messagebox.showwarning('Warning', 'Select a match first')
        return
    index = selected[0]
    if not messagebox.askyesno('Confirm', 'Delete this match?'):
        return
    matches_list.delete(index)
    matches.pop(index)
    update_stats()

def add_match():
    if not opponent_entry.get().strip():
        messagebox.showwarning('Warning', 'No opponent!')
        return
    if not barca_entry.get().isdigit() or not scored_entry.get().isdigit():
        messagebox.showwarning('Warning', 'Not digit goals')
        return
    date_parts = day_entry.get().strip().split('.')
    if len(date_parts) != 3 or not all(part.isdigit() for part in date_parts):
        messagebox.showwarning('Warning', 'Date must look like DD.MM.YYYY')
        return
    day, month, year = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
    if not (1 <= day <= 31 and 1 <= month <= 12 and len(date_parts[2]) == 4):
        messagebox.showwarning('Warning', 'Check day (1-31), month (1-12) and 4-digit year')
        return
    if not tournament.get():
        messagebox.showwarning('Warning', 'Choose a tournament')
        return
    match = {
        'opponent': opponent_entry.get().strip(),
        'barca': int(barca_entry.get()),
        'opp': int(scored_entry.get()),
        'date': day_entry.get().strip(),
        'place': place_var.get(),
        'tournament': tournament.get(),
    }
    matches.append(match)
    matches_list.insert('end', f"{match['date']}  Barca {match['barca']}:{match['opp']} {match['opponent']}  ({match['place']}, {match['tournament']})")
    opponent_entry.delete(0, 'end')
    barca_entry.delete(0, 'end')
    scored_entry.delete(0, 'end')
    day_entry.delete(0, 'end')
    place_var.set('home')
    tournament.set('')
    update_stats()    

tk.Label(root, text='Opponent:').pack()
opponent_entry = tk.Entry(root)
opponent_entry.pack()

tk.Label(root, text='Barca goals:').pack()
barca_entry = tk.Entry(root)
barca_entry.pack()

tk.Label(root, text='Opponent goals:').pack()
scored_entry = tk.Entry(root)
scored_entry.pack()

tk.Label(root, text='Date (DD.MM.YYYY):').pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Label(root, text='Venue:').pack()
place_var = tk.StringVar(value='home')
tk.Radiobutton(root, text='Home', variable=place_var, value='home').pack()
tk.Radiobutton(root, text='Away', variable=place_var, value='away').pack()

tk.Label(root, text='Tournament:').pack()
tournament = ttk.Combobox(root, values=['La Liga', 'Champions League', 'Copa del Rey'], state='readonly')
tournament.pack()

add_button = tk.Button(root, text='Add', command=add_match)
add_button.pack()

matches = []
tk.Label(root, text='Matches:').pack()
matches_list = tk.Listbox(root, height=10, width=80)
matches_list.pack()

stats_label = tk.Label(root, text='W: 0   D: 0   L: 0')
stats_label.pack()

delete_button = tk.Button(root, text='Delete selected', command=delete_match)
delete_button.pack()

root.mainloop()
