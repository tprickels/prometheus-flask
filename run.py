import csv
from datetime import date

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def run():
    new_value = request.args['value']
    if do_the_thing(new_value):
        final = f'Added the value {new_value}'
        return render_template('run.html', final=final)


def do_the_thing(new_value):
    fieldnames = ['date', 'amount']
    with open('./run.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        row = writer.writerow(dict(date=date.today(), amount=new_value))
        return row
