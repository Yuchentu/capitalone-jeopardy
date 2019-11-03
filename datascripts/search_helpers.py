from datetime import datetime, date



def search_function(stri, curr_questions):
    banned = [u'updated_at', u'invalid_count', u'created_at']
    to_ret = []
    str_input = str(stri)
    for id_,question in curr_questions.items():
        for key in question.keys():
            if key not in banned:
                try:
                    if str_input in question[key]:
                        to_ret.append(id_)
                except:
                    try:
                        if str_input == question[key]:
                            to_ret.append(id_)
                    except:
                        pass
    res = {}
    for ret in to_ret:
        res[ret] = curr_questions[ret]
    return res

def refine_date(val, printable_questions):
    to_ret = []
    for q in printable_questions:
        if q['airdate'] == val:
            to_ret.append(q)
    return to_ret

def refine_categories(category_type, curr_questions):
    to_ret = []
    for id_,question in curr_questions.items():
        try:
            temp = question[u'category'][u'title']
            cat = temp.encode('ascii', 'ignore')
            if category_type in cat:
                to_ret.append(id_)
        except:
            pass
    res = {}
    for ret in to_ret:
        res[ret] = curr_questions[ret]
    return res

def refine_difficulty(difficulty, curr_questions):
    if difficulty == "":
        return curr_questions
    to_ret = []
    for id_,question in curr_questions.items():
        if difficulty == str(question[u'value']):
            to_ret.append(id_)
    res = {}
    for ret in to_ret:
        res[ret] = curr_questions[ret]
    return res
    

def refine_daterange(start, end, printable_questions):
    to_ret = []
    if start == '' and end != '':
        for q in printable_questions:
            if q['airdate'] == end:
                to_ret.append(q)
    elif end == '' and start != '':
        for q in printable_questions:
            if q['airdate'] == start:
                to_ret.append(q)
    elif end == '' and start == '':
        return printable_questions
    else:
        for q in printable_questions:
            if start <= q['airdate'] <= end:
                to_ret.append(q)
    return to_ret





# class PrintableQuestion:
#     def __init__(self, difficulty, category, question, answer, airdate, id_, invalid_count):
#         self.difficulty = difficulty
#         self.category = category
#         self.question = question
#         self.answer = answer
#         self.airdate = airdate
#         self.id = id_
#         self.invalid_count = invalid_count
        

#difficulty, category, question, answer, airdate, id_, invalid_count
def create_printable(question):
    try:
        category = question[u'category'][u'title'].encode('ascii', 'ignore')
    except:
        category = 'Misc.'
    try:
        raw_date = question[u'airdate'].encode('ascii', 'ignore')
    except:
        return {}
    real_date = datetime.strptime(raw_date[:10], "%Y-%m-%d").date()
    vals = {}
    printables = ['value', 'question', 'answer', 'id', 'invalid_count']
    for key,item in question.items():
        act = key.encode('ascii', 'ignore')
        if act in printables:
            if act == 'value':
                vals['difficulty'] = item
            else:
                vals[act] = item
    vals['airdate'] = real_date
    vals['category'] = category
    return vals






    