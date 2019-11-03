from flask import Flask, render_template, request
import datascripts.search_helpers as helpers
import pickle
from datetime import datetime

TOT_QUESTIONS = 156809

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		if not request.form.get("symbol"):
			symbol = ""
		else:
			symbol = request.form.get("symbol")
		if not request.form.get("category"):
			category = ""
		else:
			category = request.form.get("category")
		if not request.form.get("difficulty"):
			difficulty = ""
		else:
			difficulty = request.form.get("difficulty")
		if not request.form.get("start"):
			start = ""
		else:
			start = datetime.strptime(request.form.get("start"), "%Y-%m-%d").date()
		if not request.form.get("end"):
			end = ""
		else:
			end = datetime.strptime(request.form.get("end"), "%Y-%m-%d").date()
		if not request.form.get("num_results"):
			num_results = TOT_QUESTIONS + 1
		else:
			num_results = request.form.get("num_results")

		print(start)
		print(end)

		parsed = pickle.load(open( "datascripts/file.pkl", "rb" ))
		for x,y in parsed.items():
			print(x)
			print(y)
			break


		if symbol != '':
			parsed = helpers.search_function(symbol, parsed)
		if category != '':
			parsed = helpers.refine_categories(category, parsed)
		if difficulty != '':
			parsed = helpers.refine_difficulty(difficulty, parsed)
		tot = []
		for temp in parsed.values():
			try:
				printable = helpers.create_printable(temp)
				if printable == {}:
					continue
				tot.append(printable)
			except:
				continue
		if start != '' or end != '':
			tot = helpers.refine_daterange(start, end, tot)

		if tot == []:
			return render_template('noresults.html')
		else:
			return render_template('results.html', data = tot)
		



	return render_template('base.html')


@app.route('/results', methods=['POST'])
def results():
	return render_template('results.html')



if __name__ == '__main__': app.run(debug=True)