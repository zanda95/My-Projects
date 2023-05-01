import pandas as pd
import random
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.button import Button
from urllib.request import urlopen
import json
from kivy_gradient import Gradient
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.uix.image import Image 
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    FakeCircularElevationBehavior,
    FakeRectangularElevationBehavior
)
from kivymd.uix.label import MDIcon
from random import randint, choice
from kivymd.uix.floatlayout import MDFloatLayout
import os
from kivy.graphics import *

Window.size = (350, 600)


class MD3Card(MDCard):
    # Implements a material design v3 card
    bg_color = ListProperty([1, 1,  1, 1])

class TextResultMode(MDCard):
    text_question = StringProperty()
    text_title = StringProperty()
    text_true = StringProperty()
    text_your_option = StringProperty()
    bg_color = ListProperty([1, 1,  1, 1])

    color = ListProperty([1, 1,  1, 1])
    check_color = ListProperty([1, 1,  1, 1])
    check_text = StringProperty()

    icon = StringProperty()
class ImageResultMode(MDCard):
    image_question = StringProperty()
    image_title = StringProperty()
    image_true = StringProperty()
    image_your_option = StringProperty()
    bg_color = ListProperty([1, 1,  1, 1])

    image_color = ListProperty([1, 1,  1, 1])
    check_image_color = ListProperty([1, 1,  1, 1])
    check_image_text = StringProperty()
class ImageButton2(CircularRippleBehavior, ButtonBehavior, Image):
    md_bg_color = ListProperty([1, 1,  1, 1])
    image_source = StringProperty()
class ContinentButton(CircularRippleBehavior, ButtonBehavior, Image):
    md_bg_color = ListProperty([1, 1,  1, 1])
    image_source = StringProperty()

class CircularProgressBar(AnchorLayout):
    
    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)

    set_value = NumericProperty(0)
    value= NumericProperty(0)
    bar_color = ListProperty([1, 0,  237/255]) # [1, 0, 100/255]
    bar_width = NumericProperty(10)
    text = StringProperty("0%")
    duration = NumericProperty(1)
    counter = 0


class ImageButton(Image, Button):
    image_source = StringProperty()

class CircularElevationButton(
    FakeCircularElevationBehavior,
    CircularRippleBehavior,
    ButtonBehavior,
    MDBoxLayout,
):
    pass
class CircularElevationButton_wc(
    FakeCircularElevationBehavior,
    CircularRippleBehavior,
    ButtonBehavior,
    MDBoxLayout,
):
    pass

class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        # self.ripple_scale = 0.85
        super().__init__(**kwargs)
 
class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass
class Card (MDCard):
    source = StringProperty()
    text = StringProperty()

class ButtonCard(MDCard, ButtonBehavior):
    bg_color = ListProperty([1, 1,  1, 1])
class SignButton(Button):
    bg_color = ListProperty([1, 1,  1, 1])
class OptionButton(Button):
    bg_color = ListProperty([1, 1,  1, 1]) 
class OptinCard(MDFloatLayout):
    bg_color = ListProperty([1, 1,  1, 1])
class NewOptionButton(Button):
    bg_color = ListProperty([1, 1,  1, 1])


# world cup path
wc_path = "wcfile.json"
wc_df = pd.read_json(wc_path) 
# film path
film_path = "filmfile.json"
film_df = pd.read_json(film_path) 
# history path
history_path = "historyfile.json"
history_df = pd.read_json(history_path) 
# flag path
flag_path = "flagfile.json"
flag_df = pd.read_json(flag_path) 
# country path
country_path = "countryfile.json"
country_df = pd.read_json(country_path) 


def preload_data(idx):
    #idx parm: selected randomly time and again at function call

    continent_category = "Continent"
    continent_question = country_df["countries"][idx]["country"]
    continent_correct = country_df["countries"][idx]["continent"]
    
    wc_category = "World Cup"
    wc_question = (wc_df["Info"][idx])
    wc_correct = (wc_df["Result"][idx])
    wc_wrong = (wc_df["wc_fel"][idx][0], wc_df["wc_fel"][idx][1])
    wc_correct_record = (wc_df["Record"][idx])

    film_question = film_df["results"][idx] ["question"]
    film_correct = film_df["results"][idx] ["correct_answer"]
    film_wrong = film_df["results"][idx]["incorrect_answers"][1], film_df["results"][idx]["incorrect_answers"][2]
    film_category = film_df["results"][idx] ["category"]

    history_question = history_df["results"][idx] ["question"]
    history_correct = history_df["results"][idx] ["correct_answer"]
    history_wrong = history_df["results"][idx]["incorrect_answers"][1], history_df["results"][idx]["incorrect_answers"][2]
    history_category = history_df["results"][idx] ["category"]
    
    countries_category = "Countries"
    countries_question = flag_df["country"][idx]["name"]
    countries_correct = flag_df["country"][idx]["link"]
    countries_wrong= flag_df["country"][idx+1]["link"], flag_df["country"][idx+2]["link"], flag_df["country"][idx+3]["link"]

    capital_category = "Capitals"
    capital_question = country_df["countries"][idx]["country"]
    capital_correct = country_df["countries"][idx]["capital"]
    capital_wrong= country_df["countries"][idx]["cities"][0], country_df["countries"][idx]["cities"][1]
    

    #fixing charecters with bad formatting
    formatting = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "<"),

        ("&Aring;", "Å"),
        ("&aring;", "Å"),
        ("&Ouml;", "Ö"),
        
        ("&Auml;", "Ä"),
        ("&auml;", "ä"),
        ("&#196;", "Ä"),
        ("&#228;", "ä"),
        ("&gt;", ">")
        ]

    #replace bad charecters in strings

    for tuple in formatting:
        wc_question = wc_question.replace(tuple[0], tuple[1])
        wc_correct = wc_correct.replace(tuple[0], tuple[1])

        film_question = film_question.replace(tuple[0], tuple[1])
        film_correct = film_correct.replace(tuple[0], tuple[1])

        history_question = history_question.replace(tuple[0], tuple[1])
        history_correct = history_correct.replace(tuple[0], tuple[1])

        countries_question = countries_question.replace(tuple[0], tuple[1])
        countries_correct = countries_correct.replace(tuple[0], tuple[1])
        
        continent_question = continent_question.replace(tuple[0], tuple[1])
        continent_correct = continent_correct.replace(tuple[0], tuple[1])

        capital_question = capital_question.replace(tuple[0], tuple[1])
        capital_correct = capital_correct.replace(tuple[0], tuple[1])
        
        
    #replace bad charecters in lists
    for tuple in formatting:
        wc_wrong = [char.replace(tuple[0], tuple[1]) for char in wc_wrong]
        film_wrong = [char.replace(tuple[0], tuple[1]) for char in film_wrong]
        history_wrong = [char.replace(tuple[0], tuple[1]) for char in history_wrong]
        countries_wrong = [char.replace(tuple[0], tuple[1]) for char in countries_wrong]
        capital_wrong = [char.replace(tuple[0], tuple[1]) for char in capital_wrong]
        
    
    parameters["wc_question"].append(wc_question)
    parameters["wc_correct"].append(wc_correct)
    parameters["wc_category"].append(wc_category)

    parameters["film_question"].append(film_question)
    parameters["film_correct"].append(film_correct)
    parameters["film_category"].append(film_category)

    parameters["history_question"].append(history_question)
    parameters["history_correct"].append(history_correct)
    parameters["history_category"].append(history_category)

    parameters["countries_question"].append(countries_question)
    parameters["countries_correct"].append(countries_correct)
    parameters["countries_category"].append(countries_category)
    
    parameters["continent_question"].append(continent_question)
    parameters["continent_correct"].append(continent_correct)
    parameters["continent_category"].append(continent_category)  

    parameters["capital_question"].append(capital_question)
    parameters["capital_correct"].append(capital_correct)
    parameters["capital_category"].append(capital_category)

    wc_all_answers = wc_wrong + [wc_correct]
    film_all_answers = film_wrong + [film_correct]
    history_all_answers = history_wrong + [history_correct]
    countries_all_answers = countries_wrong + [countries_correct]
    capital_all_answers = capital_wrong + [capital_correct]
    

    random.shuffle(wc_all_answers)
    random.shuffle(film_all_answers)
    random.shuffle(history_all_answers)
    random.shuffle(countries_all_answers)
    random.shuffle(capital_all_answers)

    parameters["wc_answer1"].append(wc_all_answers[0])
    parameters["wc_answer2"].append(wc_all_answers[1])
    parameters["wc_answer3"].append(wc_all_answers[2])

    parameters["film_answer1"].append(film_all_answers[0])
    parameters["film_answer2"].append(film_all_answers[1])
    parameters["film_answer3"].append(film_all_answers[2])

    parameters["history_answer1"].append(history_all_answers[0])
    parameters["history_answer2"].append(history_all_answers[1])
    parameters["history_answer3"].append(history_all_answers[2])

    parameters["capital_answer1"].append(capital_all_answers[0])
    parameters["capital_answer2"].append(capital_all_answers[1])
    parameters["capital_answer3"].append(capital_all_answers[2])

    parameters["countries_answer1"].append(countries_all_answers[0])
    parameters["countries_answer2"].append(countries_all_answers[1])
    parameters["countries_answer3"].append(countries_all_answers[2])
    parameters["countries_answer4"].append(countries_all_answers[3])
  

    

#dictionary to store local pre-load parameters on a global level
parameters = {
    "wc_category": [],
    "wc_question": [],
    "wc_correct": [],
    "wc_answer1": [],
    "wc_answer2": [],
    "wc_answer3": [],

    "film_category": [],
    "film_question": [],
    "film_correct": [],
    "film_answer1": [],
    "film_answer2": [],
    "film_answer3": [],

    "history_category": [],
    "history_question": [],
    "history_correct": [],
    "history_answer1": [],
    "history_answer2": [],
    "history_answer3": [],

    "countries_category": [],
    "countries_question": [],
    "countries_correct": [],
    "countries_answer1": [],
    "countries_answer2": [],
    "countries_answer3": [],
    "countries_answer4": [],

    "capital_category": [],
    "capital_question": [],
    "capital_correct": [],
    "capital_answer1": [],
    "capital_answer2": [],
    "capital_answer3": [],
    
    "continent_category": [],
    "continent_question": [],
    "continent_correct": [],

    "correct": [],

    "score": [],
    "index": []
    }



class QuizApp(MDApp):
    parameters["index"].append(random.randint(0,25))

    selected_sign = ""
    answer = ""
    correct = 0
    wrong = 0
    que_count = 0
    current = 0
    count_of_question = 5

    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition=NoTransition())

        self.title= "Trivia Quest"
        
        screen_manager.add_widget(Builder.load_file("start.kv"))
        screen_manager.add_widget(Builder.load_file("select_sign.kv"))
        screen_manager.add_widget(Builder.load_file("trivia.kv"))
        screen_manager.add_widget(Builder.load_file("flagscreen.kv"))
        screen_manager.add_widget(Builder.load_file("continent_screen.kv"))
        screen_manager.add_widget(Builder.load_file("winner.kv"))
        screen_manager.add_widget(Builder.load_file("sign.kv"))
        screen_manager.add_widget(Builder.load_file("alla_que.kv"))
        screen_manager.add_widget(Builder.load_file("final_score.kv"))
        return screen_manager

    def select_que(self, sign):
        self.selected_sign = sign

        if sign == "Entertainment: Film":
            screen_manager.get_screen("quiz").ids.titel.text= f"{sign}"
            parameters["index"].pop()
            parameters["index"].append(random.randint(0,25))
            preload_data(parameters["index"][-1])
            screen_manager.get_screen("quiz").ids.question.text = parameters["film_question"][-1]
            self.answer = parameters["film_correct"][-1]
            
            screen_manager.get_screen("quiz").ids.option1.text= parameters["film_answer1"][-1]
            screen_manager.get_screen("quiz").ids.option2.text= parameters["film_answer2"][-1]
            screen_manager.get_screen("quiz").ids.option3.text= parameters["film_answer3"][-1]
            screen_manager.current = "quiz"
            
        elif sign == "History":
            screen_manager.get_screen("quiz").ids.titel.text= f"{sign}"
            parameters["index"].pop()
            parameters["index"].append(random.randint(0,25))
            preload_data(parameters["index"][-1])
            screen_manager.get_screen("quiz").ids.question.text = parameters["history_question"][-1]
            self.answer = parameters["history_correct"][-1]
            
            screen_manager.get_screen("quiz").ids.option1.text= parameters["history_answer1"][-1]
            screen_manager.get_screen("quiz").ids.option2.text= parameters["history_answer2"][-1]
            screen_manager.get_screen("quiz").ids.option3.text= parameters["history_answer3"][-1]
            screen_manager.current = "quiz"
        elif sign == "World Cup":

            screen_manager.get_screen("quiz").ids.titel.text= f"{sign}"
            parameters["index"].pop()
            parameters["index"].append(random.randint(0,30))
            preload_data(parameters["index"][-1])
            screen_manager.get_screen("quiz").ids.question.text = parameters["wc_question"][-1]
            self.answer = parameters["wc_correct"][-1]
            
            screen_manager.get_screen("quiz").ids.option1.text= parameters["wc_answer1"][-1]
            screen_manager.get_screen("quiz").ids.option2.text= parameters["wc_answer2"][-1]
            screen_manager.get_screen("quiz").ids.option3.text= parameters["wc_answer3"][-1]
            screen_manager.current = "quiz"
            
        elif sign == "Capitals of the World":
            screen_manager.get_screen("quiz").ids.titel.text= f"{sign}"
            parameters["index"].pop()
            parameters["index"].append(random.randint(0,25))
            preload_data(parameters["index"][-1])
            screen_manager.get_screen("quiz").ids.question.text = "What is the capital of "+ parameters["capital_question"][-1]+ "?"
            self.answer = parameters["capital_correct"][-1]
            screen_manager.get_screen("quiz").ids.option1.text= parameters["capital_answer1"][-1]
            screen_manager.get_screen("quiz").ids.option2.text= parameters["capital_answer2"][-1]
            screen_manager.get_screen("quiz").ids.option3.text= parameters["capital_answer3"][-1]
            screen_manager.current = "quiz"
            
        elif sign == "Flags of the World":
            screen_manager.get_screen("Flags of the World").ids.titel.text= f"{sign}"
            parameters["index"].pop()
            parameters["index"].append(random.randint(0,30))
            preload_data(parameters["index"][-1])
            self.answer = parameters["countries_correct"][-1]
            
            screen_manager.get_screen("Flags of the World").ids.flag_toolbar.text= "What is the flag of " + parameters["countries_question"][-1] + "?"
            screen_manager.get_screen("Flags of the World").ids.country0.source= parameters["countries_answer1"][-1]
            screen_manager.get_screen("Flags of the World").ids.country1.source= parameters["countries_answer2"][-1]
            screen_manager.get_screen("Flags of the World").ids.country2.source= parameters["countries_answer3"][-1]
            screen_manager.get_screen("Flags of the World").ids.country3.source= parameters["countries_answer4"][-1]
            screen_manager.current = "Flags of the World"
            
        elif sign == "Continents of the World":
            screen_manager.get_screen("Continents of the World").ids.titel.text= f"{sign}"
            parameters["index"].pop()
            parameters["index"].append(random.randint(0,30))
            preload_data(parameters["index"][-1])
            self.answer = parameters["continent_correct"][-1]
            screen_manager.get_screen("Continents of the World").ids.continent_toolbar.text= "In which continent lies " + parameters["continent_question"][-1] + "?"
            screen_manager.get_screen("Continents of the World").ids.continen0.source= "data/\continents/Asia.png"
            screen_manager.get_screen("Continents of the World").ids.continen1.source= "data/\continents/Africa.png"
            screen_manager.get_screen("Continents of the World").ids.continen2.source= "data/\continents/Europe.png"
            screen_manager.get_screen("Continents of the World").ids.continen3.source= "data/\continents/North America.png"
            screen_manager.get_screen("Continents of the World").ids.continen4.source= "data/\continents/South America.png"
            screen_manager.get_screen("Continents of the World").ids.continen5.source= "data/\continents/Oceania.png"
            screen_manager.current = "Continents of the World"
            
    
    def get_id(self, instance): 
        for id, widget in instance.parent.parent.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def counted(self):
        if self.que_count == self.count_of_question: 
            print ("Antal korrekt:", self.correct)
            print ("Antal wrong: ", self.wrong)
            if (self.correct) > (self.wrong):
                
                success_rate = round((self.correct/(self.correct+self.wrong))*100)
                screen_manager.get_screen("winner").test_bar.value = success_rate
                screen_manager.get_screen("winner").test_bar.set_value = success_rate
                screen_manager.get_screen("winner").test_bar.text = f"{success_rate}%"
                screen_manager.get_screen("winner").correct.text = f"{self.correct}"
                screen_manager.get_screen("winner").wrong.text = f"{self.wrong}"
                screen_manager.get_screen("winner").image.source="medal.png"
                screen_manager.current = "winner"
            
            elif (self.correct) < (self.wrong):
                success_rate = round((self.correct/(self.correct+self.wrong))*100)
                screen_manager.get_screen("winner").test_bar.value = success_rate
                screen_manager.get_screen("winner").test_bar.set_value = success_rate
                screen_manager.get_screen("winner").test_bar.text = f"{success_rate}%"
                screen_manager.get_screen("winner").correct.text = f"{self.correct}"
                screen_manager.get_screen("winner").wrong.text = f"{self.wrong}"
                screen_manager.get_screen("winner").image.source="meh.png"
                screen_manager.current = "winner"
            screen_manager.get_screen("winner").antal.text = f"{self.que_count}"

    def nya_quiz(self, option, instance):
        self.root.get_screen(self.selected_sign).ids.flags_bottom_bar.disabled = False
        self.root.get_screen(self.selected_sign).ids.flags_forward.opacity = 1
        self.root.get_screen(self.selected_sign).ids.progress1.value -= 100/self.count_of_question
        self.que_count += 1
       

        if self.selected_sign == "Flags of the World":
            image_question = "What is the flag of "+ parameters["countries_question"][-1]+ "?"
            image_title = (self.selected_sign)
            image_true = parameters["countries_correct"][-1]

            if option == self.answer:
                self.correct += 1
                screen_manager.get_screen("alla_que.kv").ids.grid.add_widget(ImageResultMode
                (image_question=f"{image_question}", image_title=f"{image_title}", image_true=f"{image_true}", image_your_option= option, image_color = (2/255, 203/255, 2/255, 1),
                check_image_text = "check-circle-outline", check_image_color = get_color_from_hex("02cb02") )
                )
                # Green color
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].md_bg_color = (0, 1, 0, 1)
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].disabled= True
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].disabled_color= get_color_from_hex("2c382d")
                option_id_list = ["country0", "country1", "country2", "country3"]
                option_id_list.remove(self.get_id(instance))
                for i in range(0, 3):
                    screen_manager.get_screen(self.selected_sign).ids[f"{option_id_list[i]}"].disabled= True
                    screen_manager.get_screen(self.selected_sign).ids[f"{option_id_list[i]}"].disabled_color= get_color_from_hex("2c382d") 
                    

            else:
                self.wrong += 1

                screen_manager.get_screen("alla_que.kv").ids.grid.add_widget(ImageResultMode
                (image_question=f"{image_question}", image_title=f"{image_title}", image_true=f"{image_true}", image_your_option= option, image_color = (255/255, 0/255, 0/255, 1),
                check_image_text = "minus-circle-outline", check_image_color = get_color_from_hex("ff0000") ))
                
                for i in range(0, 4):
                    if screen_manager.get_screen(self.selected_sign).ids[f"country{i}"].source == self.answer:
                        screen_manager.get_screen(self.selected_sign).ids[f"country{i}"].disabled= True
                        screen_manager.get_screen(self.selected_sign).ids[f"country{i}"].disabled_color= get_color_from_hex("2c382d")  
                        screen_manager.get_screen(self.selected_sign).ids[f"country{i}"].md_bg_color = (0, 1, 0, 1)
                    else:
                        screen_manager.get_screen(self.selected_sign).ids[f"country{i}"].disabled= True
                        screen_manager.get_screen(self.selected_sign).ids[f"country{i}"].disabled_color= get_color_from_hex("2c382d") 
                        
                #Red color
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].md_bg_color = get_color_from_hex("f75e05") 
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].disabled_color= get_color_from_hex("2c382d")
        elif self.selected_sign == "Continents of the World":
            image_question = "In which continent lies " + parameters["continent_question"][-1] + "?"
            
            image_title = (self.selected_sign)
            image_true = "data/\continents/" + str(self.answer)+".png"
            
            
            if option == "data/\continents/" + str(self.answer)+".png":
                
                self.correct += 1

                screen_manager.get_screen("alla_que.kv").ids.grid.add_widget(ImageResultMode
                (image_question=f"{image_question}", image_title=f"{image_title}", image_true=f"{image_true}", image_your_option= option, image_color = (2/255, 203/255, 2/255, 1),
                check_image_text = "check-circle-outline", check_image_color = get_color_from_hex("02cb02") )
                )
                
                # Green color
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].md_bg_color = (0, 1, 0, 1)
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].disabled= True
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].disabled_color= get_color_from_hex("2c382d")
    
                option_id_list = ["continen0", "continen1", "continen2", "continen3", "continen4", "continen5"]
                option_id_list.remove(self.get_id(instance))
                for i in range(0, 5):
                    screen_manager.get_screen(self.selected_sign).ids[f"{option_id_list[i]}"].disabled= True
                    screen_manager.get_screen(self.selected_sign).ids[f"{option_id_list[i]}"].disabled_color= get_color_from_hex("2c382d") 
            else:
                self.wrong += 1
                
                screen_manager.get_screen("alla_que.kv").ids.grid.add_widget(ImageResultMode
                (image_question=f"{image_question}", image_title=f"{image_title}", image_true=f"{image_true}", image_your_option= option, image_color = (255/255, 0/255, 0/255, 1),
                check_image_text = "minus-circle-outline", check_image_color = get_color_from_hex("ff0000") ))

                for i in range(0, 6):
                    if screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].source == "data/\continents/" + str(self.answer)+".png":
                        screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].disabled= True
                        screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].disabled_color= get_color_from_hex("2c382d")  
                        screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].md_bg_color = (0, 1, 0, 1)
                    else:
                        screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].disabled= True
                        screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].disabled_color= get_color_from_hex("2c382d") 
                        
                #Red color
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].md_bg_color = get_color_from_hex("f75e05") 
                screen_manager.get_screen(self.selected_sign).ids[self.get_id(instance)].disabled_color= get_color_from_hex("2c382d")

         
        self.counted() 
        

    def quiz(self, option, instance):
        self.root.get_screen("quiz").ids.flags_bottom_bar.disabled = False
        self.root.get_screen("quiz").ids.flags_forward.opacity = 1
        self.root.get_screen("quiz").ids.progress1.value -= 100/self.count_of_question
        self.que_count += 1

        def check_asnwer():
            if str(option) == f"{text_true}":
                screen_manager.get_screen("alla_que.kv").ids.grid.add_widget(TextResultMode
                    (text_question=f"{text_question}", text_title=f"{text_title}", text_true=f"{text_true}", text_your_option="Correct answner!" , color= (2/255, 203/255, 2/255, 1), check_text = "check-circle-outline", check_color = get_color_from_hex("02cb02") )
                    )
            else: 
                screen_manager.get_screen("alla_que.kv").ids.grid.add_widget(TextResultMode
                    (text_question=f"{text_question}", text_title=f"{text_title}", text_true=f"{text_true}", text_your_option="Wrong answer! You answered: " + str(option), 
                    color= (255/255, 0/255, 0/255, 1), check_text = "minus-circle-outline", check_color = get_color_from_hex("ff0000") )
                    )
            
            
        if self.selected_sign == "Entertainment: Film":
            text_question= parameters["film_question"][-1]
            text_title= (self.selected_sign)
            text_true= parameters["film_correct"][-1]
            check_asnwer()
            
        elif self.selected_sign == "History":
            text_question= parameters["history_question"][-1]
            text_title= (self.selected_sign)
            text_true= parameters["history_correct"][-1]
            check_asnwer()
        elif self.selected_sign == "World Cup":
            text_question= parameters["wc_question"][-1]
            text_title= (self.selected_sign)
            text_true= parameters["wc_correct"][-1]
            check_asnwer()
        elif self.selected_sign == "Capitals of the World":
            text_question= "What is the capital of " + parameters["capital_question"][-1] + "?"
            text_title= (self.selected_sign)
            text_true= parameters["capital_correct"][-1]
            check_asnwer()
        
        if option == self.answer:
            self.correct += 1
            
            # Green color
            screen_manager.get_screen("quiz").ids[self.get_id(instance)].bg_color = (0, 1, 0, 1)
            screen_manager.get_screen("quiz").ids[self.get_id(instance)].disabled= True
            screen_manager.get_screen("quiz").ids[self.get_id(instance)].disabled_color= get_color_from_hex("2c382d")
            option_id_list = ["option1", "option2", "option3"]
            option_id_list.remove(self.get_id(instance))
            for i in range(0, 2):
                screen_manager.get_screen("quiz").ids[f"{option_id_list[i]}"].disabled= True
                screen_manager.get_screen("quiz").ids[f"{option_id_list[i]}"].disabled_color= get_color_from_hex("2c382d") 
                

        else:
            self.wrong += 1
            for i in range(1, 4):
                if screen_manager.get_screen("quiz").ids[f"option{i}"].text == self.answer:
                    screen_manager.get_screen("quiz").ids[f"option{i}"].disabled= True
                    screen_manager.get_screen("quiz").ids[f"option{i}"].disabled_color= get_color_from_hex("2c382d")  
                    screen_manager.get_screen("quiz").ids[f"option{i}"].bg_color = (0, 1, 0, 1)
                else:
                    screen_manager.get_screen("quiz").ids[f"option{i}"].disabled= True
                    screen_manager.get_screen("quiz").ids[f"option{i}"].disabled_color= get_color_from_hex("2c382d") 
                    
            #Red color
            screen_manager.get_screen("quiz").ids[self.get_id(instance)].bg_color = get_color_from_hex("f75e05") 
            screen_manager.get_screen("quiz").ids[self.get_id(instance)].disabled_color= get_color_from_hex("2c382d")

            
        self.counted()  
        
        
    def disable_flags_bottom_bar(self):
        self.root.get_screen('quiz').ids.flags_forward.opacity = 0
    def new_disable_flags_bottom_bar(self):
        self.root.get_screen('Flags of the World').ids.flags_forward.opacity = 0
    def disable_continent_bottom_bar(self):
        self.root.get_screen('Continents of the World').ids.flags_forward.opacity = 0

    def nasta_question(self):
        self.select_que(self.selected_sign)
        for i in range(1, 4):    
            screen_manager.get_screen("quiz").ids[f"option{i}"].disabled= False
            screen_manager.get_screen("quiz").ids[f"option{i}"].bg_color = get_color_from_hex("c1cbe3")
            screen_manager.get_screen("quiz").ids[f"option{i}"].disabled_color= (1, 1, 1, 0.3)
    def nasta_bild(self):
        self.select_que(self.selected_sign)
        for i in range(0, 4):    
            screen_manager.get_screen("Flags of the World").ids[f"country{i}"].disabled= False
            screen_manager.get_screen("Flags of the World").ids[f"country{i}"].md_bg_color = get_color_from_hex("c1cbe3")
            screen_manager.get_screen("Flags of the World").ids[f"country{i}"].disabled_color= (1, 1, 1, 0.3)
    def next_continent(self):
        self.select_que(self.selected_sign)
        for i in range(0, 6):    
            screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].disabled= False
            screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].md_bg_color = get_color_from_hex("c1cbe3")
            screen_manager.get_screen(self.selected_sign).ids[f"continen{i}"].disabled_color= (1, 1, 1, 0.3)
        
    def final_score(self):
        if self.correct ==0 and self.wrong==0:
            screen_manager.current = "start"
            for i in range(1, 4):    
                screen_manager.get_screen("quiz").ids[f"option{i}"].disabled= False
                screen_manager.get_screen("quiz").ids[f"option{i}"].bg_color = get_color_from_hex("f5f5f5")
                screen_manager.get_screen("quiz").ids[f"option{i}"].disabled_color= (1, 1, 1, 0.3)
                
            screen_manager.get_screen("final_score").correct.text = "0 !"
            screen_manager.get_screen("final_score").wrong.text = "0 "
            screen_manager.get_screen("final_score").success_rate.text = "0% Success!"
            screen_manager.current = "final_score"
        else:
            for i in range(1, 4):    
                screen_manager.get_screen("quiz").ids[f"option{i}"].disabled= False
                screen_manager.get_screen("quiz").ids[f"option{i}"].bg_color = get_color_from_hex("f5f5f5")
                screen_manager.get_screen("quiz").ids[f"option{i}"].disabled_color= (1, 1, 1, 0.3)
            success_rate = round((self.correct/(self.correct+self.wrong))*100)
            screen_manager.get_screen("final_score").correct.text = f"{self.correct} "
            screen_manager.get_screen("final_score").wrong.text = f"{self.wrong}"
            screen_manager.get_screen("final_score").success_rate.text = f"{success_rate}% Success!"
            screen_manager.current = "final_score"

    def move(self):
        screen_manager.current = "alla_que.kv"
    def replay(self):
        for i in range(1, 4):    
            screen_manager.get_screen("quiz").ids[f"option{i}"].disabled= False
            screen_manager.get_screen("quiz").ids[f"option{i}"].bg_color = get_color_from_hex("c1cbe3")
            screen_manager.get_screen("quiz").ids[f"option{i}"].disabled_color= (1, 1, 1, 0.3)
        for i in range(0, 4):    
            screen_manager.get_screen("Flags of the World").ids[f"country{i}"].disabled= False
            screen_manager.get_screen("Flags of the World").ids[f"country{i}"].md_bg_color = get_color_from_hex("c1cbe3")
            screen_manager.get_screen("Flags of the World").ids[f"country{i}"].disabled_color= (1, 1, 1, 0.3)

        for i in range(0, 6):    
            screen_manager.get_screen("Continents of the World").ids[f"continen{i}"].disabled= False
            screen_manager.get_screen("Continents of the World").ids[f"continen{i}"].md_bg_color = get_color_from_hex("c1cbe3")
            screen_manager.get_screen("Continents of the World").ids[f"continen{i}"].disabled_color= (1, 1, 1, 0.3)

        self.root.get_screen('quiz').ids.progress1.value = 100
        self.root.get_screen('Flags of the World').ids.progress1.value = 100
        self.root.get_screen('Continents of the World').ids.progress1.value = 100

        self.disable_flags_bottom_bar()
        self.new_disable_flags_bottom_bar()
        self.disable_continent_bottom_bar()
        
        self.root.get_screen('quiz').ids.flags_bottom_bar.disabled = True
        self.root.get_screen('Flags of the World').ids.flags_bottom_bar.disabled = True
        self.root.get_screen('Continents of the World').ids.flags_bottom_bar.disabled = True
        
        self.correct = 0
        self.wrong = 0
        self.que_count = 0
        screen_manager.current = "start"

if __name__ == '__main__': 
    QuizApp().run()
