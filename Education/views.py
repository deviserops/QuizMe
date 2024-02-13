# import render to render an HTML template with a given context and return an HttpResponse object
from multiprocessing import context
from unittest import result

# use get_object_or_404 in views.py to render a HTTP 404 error if a question with the requested ID doesn’t exist
from django.shortcuts import get_object_or_404, render

# import html to handle potential HTML entities and aid rendering
import html

# Import the login required decorator to prevent unaouthorised access to cetrain views.
from django.contrib.auth.decorators import login_required

# imported HttpResponseRedirect 
from django.http import HttpResponseRedirect

# imported reverse
from django.urls import reverse

# import functions from utils.py called in views
from .utils import get_json_categories, get_specific_json_category, get_next_question_id, get_category_names, category_objects

# import models
from .models import *

# import apps to dynamically fetch a model in detail() view
from django.apps import apps

# import Http404 to raise an error message if a model is not located in detail view
from django.http import Http404

# import random to shuffle questions in detail view, rendered in the form
import random

# import logging for debugging
import logging

# import ast safely evaluate strings containing Python literal structures e.g.strings, lists, dicts
# use to convert str into list
import ast 

#######################################################################################
#######################################################################################

# Create your views here.

'''
Create a view for the home page of QuizMe project.
'''
# define index view for home page of QuizMe project referenced in Education/urls.py
def index(request):     
    # Render your template and map a URL to it
    return render(request, "index.html")

'''
Create a view for the home page of education quizzes.
'''
# display the category of the education quiz
# https://www.youtube.com/watch?v=sgEhb50YSTE
# make the category_id a parameter set to None
# get json reponse for trivia categories from open trivia db
# index category from the dictionary id
def index_edu(request):
    # call the categories function & save its response in an assigned variable - NameError if you don't assign it
    response = get_json_categories()
            
    # call the function to return the chosen categories to present a quiz for on the homepage
    category_name = get_category_names(response)       

    # call the function to retrieve the objects from the django database - viewable on admin site
    question_selection =  category_objects(request, category_name)    

    # the response is the dictionary for trivia categories
    # pass all the context variables into a single dictionary to render in the template correctly
    context = {'category_name': category_name,               
               'question_selection': question_selection
               }            
    
    # render the context to the homepage of education
    return render(request, 'edu_quiz/edu_quiz.html', context) 

# write a view for the quiz question, incl the argument question_id
# question_id is the specific identifier passed in the URL when accessing this view
# it uniquely identifies and retrieves the specific question to display
# Django automatically adds an id field as the primary key for each model (i.e. question.id)
# display the question text 
# render an HTTP 404 error if a question with the requested ID doesn’t exist
def detail(request, category_name, question_id):  
    response = get_json_categories()
    category_name = get_category_names(response)  
    # use the category_name selected on edu_quiz.html to determine the model to get questions from
    # replace spaces in the event category names have spaces to create a valid model name
    model_name = category_name.replace(" ", "_")

    # use a try-except block to find a model that matches the category name
    # use apps module to dynamically retrieve a model
    # - dynamically:instead of explicitly specifying a fixed model in the code, generate or determine the model to use at runtime based on certain conditions/data
    try:
        model = apps.get_model('Education', model_name)
    except LookupError:
        raise Http404("Cannot locate the model for the selected category.")     
    
    question = get_object_or_404(model, pk=question_id)    
    
    # use the helper function literal_eval of the ast module to convert the str representation of the choices list
    # - in the textfield of the category model into a list
    # https://python.readthedocs.io/en/latest/library/ast.html#ast.literal_eval
    # note:ast.literal_eval is safer than eval. it only evaluates literals & not arbitrary expressions, 
    # - reducing the risk of code injection
    # use in template to iterate over the list of choices dictionaries and access the values for the 'choice' key
    convert_choices_textfield_into_list = ast.literal_eval(question.choices)    

    # render the edu_detail template & pass the 10 questions, their ids & category as context 
    context = {'question': question,
               'choices':convert_choices_textfield_into_list,
               'category_name': category_name 
               }
    
    return render(request, 'edu_quiz/edu_detail.html', context)

'''
Create a view that displays the quiz result.
'''
# create a view that displays the quiz result 
def results(request, category_name): 
    # get the quiz result for the session
    result = request.session.get('quiz_result')
           
    # render the result template  
    # pass the quiz result for the session as a context variable
    context = {'result':result,
               'category_name': category_name
               }   
    return render(request, 'edu_quiz/edu_result.html', context)

# write a view to answer a question, incl the argument question_id
# it handles the submitted data
def selection(request, category_name, question_id):    
    # pk refers to the primary key field of a database table
    # django automatically creates a primary key for each model
    response = get_json_categories()
    category_name = get_category_names(response)
    model_name = category_name.replace(" ", "_")
    model = apps.get_model('Education', model_name)
    question = get_object_or_404(model, pk=question_id)
    #    
    print(f"correct_answer:{question.correct_answer}")    
    # use the helper function literal_eval of the ast module to convert the str representation of the choices list
    # - in the textfield of the category model into a list
    # https://python.readthedocs.io/en/latest/library/ast.html#ast.literal_eval
    # note:ast.literal_eval is safer than eval. it only evaluates literals & not arbitrary expressions, 
    # - reducing the risk of code injection
    # use in template to iterate over the list of choices dictionaries and access the values for the 'choice' key
    convert_choices_textfield_into_list = ast.literal_eval(question.choices)             
        
    # access submitted data by key name with a dictionary-like object- request.POST
    # use the key name 'choice' (defined in edu_detail form input) which returns the ID of the selected choice
    # retrieve the selected choice instance from the database based on the primary key
    # - obtained from the 'choice' key in the submitted form data (request.POST)
    # assumes that the 'id' attribute of the choice in the model is an integer
    try:
        selected_choice = model.objects.get(
            pk=request.POST['choice']
            )
        
    # raise a KeyError if the ID of the choice isn’t found
    # an error occurs if the mapping (dictionary) key was not located in the set of existing keys
    except (KeyError, model.DoesNotExist):        
        # Redisplay the question voting form
        return render(request, 'edu_quiz/edu_detail.html', {
            'category_name': category_name,
            'question': question,
            'choices': convert_choices_textfield_into_list,
            'error_message': "You didn't select a choice."
            })
    
    else:
        result = 0
        # iterate over the list of dictionaries for choices and compare the 'id' values
        # check if the id in the queryset for choices is 1 & that the id for the selected_choice is 1                      
        # (in utils.py the id for the correct answer is 1)
        # else add the point for a correct choice & save the choice        
        for choice_dict in convert_choices_textfield_into_list:
            if selected_choice.id and choice_dict['id'] == 1: 
                result += 1
                selected_choice.save()

        ## retrieve question_selection_pks from the session (from utils.category_objects)
        question_selection_pks = request.session['question_selection_ids']
        ##get_context_index_edu = index_edu(request)                
        ##print(f"get_context_index_edu:{get_context_index_edu}")
        ##question_selection = get_context_index_edu.get('question_selection')        
        print(f"question_selection_ids in session:{question_selection_pks}")

        # get the next question
        next_question = get_next_question_id(category_name, question_id, question_selection_pks)

        # if there is another question available from the question_selection redirect to the detail view again
        # - to display that question 
        if next_question is not None:
            return HttpResponseRedirect(
                reverse('Education:edu_detail', category_name=category_name, question_id=next_question)
                )

        else:
            # store the calculated result in the session
            request.session['quiz_result'] = result

            # use HttpResponseRedirect instead of HttpResponse;
            # HttpResponseRedirect takes the URL to which the user will be redirected as an argument
            # Always return an HttpResponseRedirect after successfully
            # dealing with POST data. This prevents data from being
            # posted twice if a user hits the Back button.
            # use reverse function to take the name of the view and return the str value that represents the actual url                        
            # put a comma after category_name since its a str & needs to be treated as a tuple by args 
            # - resolves NoReverseMatch error
            return HttpResponseRedirect(
                reverse('Education:results', args=(category_name,))
                )

# start new quiz function
def try_new_quiz(request):
    # delete the result & session data of the current quiz before starting a new quiz
    if 'quiz_result' in request.session:
        del request.session['quiz_result']

    # render the template for the home page of education      
    return HttpResponseRedirect(
                reverse('Education:index_edu')
                )  
        

