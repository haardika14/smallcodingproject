from rich.console import Console
from rich.table import Table
from datetime import date
while True:
    console = Console()
    table = Table(title="Mood Journal")
    table.add_column("Date")
    y = table.add_column("Mood")
    table.add_column("Note")
    table.add_row("2026-10-28", "[green]4[/green]", "Finished a good book")
    console.print(table)
    mood_input = input("What's your mood level? ")
    note_input = input("Add a quick note: ")
    current_date = str(date.today()) 
    table.add_row(current_date, f"[yellow]{mood_input}[/yellow]", note_input)
    console.print(table)
    user_input = input("Want to quit? ")
    
    if user_input == 'yes':
        print("Goodbye")
        break
    