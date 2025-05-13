font = pygame.font.Font(r"C:\Users\ARMAN\Downloads\game1\Noto_Sans_Armenian\NotoSansArmenian-VariableFont_wdth,wght.ttf", 24)

characters = {
    
    "Կառոբկա Աշոտ": {

        "pos": [580, 340],
        "size": (130, 180),
        "image_path": r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Ashot_Neutral.png",
        "dialogues": {
            "start": {
                "text": "Կինս երեկ ուզում էր սպանել ինձ,"
                " հորդ նկարած նախագահն էլ մյուս կողմից",
                "choices": [
                    {"text": "Կինդ? Բայց ինչի համար?", "next": "good_response"},
                    {"text": "Նախագահ? Բայց հայրս ասած Ազնավուրն է...", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Հաաա Նոր էի պադյեզդից դուրս եկել, մեկ էլ կիռպիչը ուղիղ գլխիս",
                "choices": [
                    {"text": "Սարսափելի է", "next": "remember_good"},
                    {"text": "ավելի լավ է, բաժանվես ու պարտքերդ մարես", "next": "remember_none"}
                ]
            },
            "tired_response": {
                "text": "Ինչ էս խոսում, իսկը նա է, Անիծված կառոբկի տերը",
                "choices": [
                    {"text": "Միգուցե և դու ճիշտ ես", "next": "remember_good"},
                    {"text": "Ինչ Կառոբկա? Ամեն ինչ կարգին է?", "next": "remember_none"}
                ]
            },
            "remember_none": {
                "text": " ՈՉԻՆՉ ԷԼ ԿԱՐԳԻՆ ՉԷ, ՔԱՂԱՔԸ ԿԱՌՈԲԿԱ Է՝ ՄԵԾ ԿԱՌՈԲԿԱ, ԻՄ ԱՉՔԵՐՈՎ ԵՄ ՏԵՍԵԼ", 
            },
            "remember_good": {
                "text": "ճիշտ եմ, ճիշտ իմ ասածները միշտ ճիշտ են",
            }
        },
        "interactable": True,
        "visible": True
    },
    "Երանյան Աշոտ": {
       "pos": [420, 355],
       "size": (130, 180),
        "image_path": r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Eranyan.png",
        "dialogues": {
            "start": {
                "text": "Բարև ջան։ Ինչպե՞ս",
                "choices": [
                    {"text": "Բարև, լավ եմ։", "next": "good_response"},
                    {"text": "Հոգնած եմ...", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Ուրախ եմ լսել դա։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "tired_response": {
                "text": "Հանգստացիր մի քիչ։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "remember_good": {
                "text": "Այնտեղի լիճը զարմանալի էր։ Հիշու՞մ ես նավակով զբոսանքը։",
                "choices": [
                    {"text": "Այո, դա երբեք չեմ մոռանա։", "next": None},
                    {"text": "Մի քիչ, բայց շատ լավ էր։", "next": None}
                ]
            },
            "remember_none": {
                "text": "Շատ վատ։ Հաջորդ անգամ կփորձենք նոր հիշողություններ ստեղծել։",
                "choices": [
                    {"text": "Լավ գաղափար է։", "next": None},
                    {"text": "Միգուցե։", "next": None}
                ]
            }
        },
        "interactable": True,
        "visible": True
    },
    "Օպոզիցիա Տիգրան": {
    
        "pos": [340, 340],
        "size": (130, 180),
        "image_path": r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Tigran.png",
        "dialogues": {
            "start": {
                "text": "Բարև ջան։ Ինչպե՞ս ես։",
                "choices": [
                    {"text": "Բարև, լավ եմ։", "next": "good_response"},
                    {"text": "Հոգնած եմ...", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Ուրախ եմ լսել դա։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "tired_response": {
                "text": "Հանգստացիր մի քիչ։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "remember_good": {
                "text": "Այնտեղի լիճը զարմանալի էր։ Հիշու՞մ ես նավակով զբոսանքը։",
                "choices": [
                    {"text": "Այո, դա երբեք չեմ մոռանա։", "next": None},
                    {"text": "Մի քիչ, բայց շատ լավ էր։", "next": None}
                ]
            },
            "remember_none": {
                "text": "Շատ վատ։ Հաջորդ անգամ կփորձենք նոր հիշողություններ ստեղծել։",
                "choices": [
                    {"text": "Լավ գաղափար է։", "next": None},
                    {"text": "Միգուցե։", "next": None}
                ]
            }
        },
        "interactable": True,
        "visible": True
    },
    "Գրիգ": {
        "pos": [200, 480],
        "size": (80, 120),  # Larger size for better visibility
        "image_path": r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Grig.png",  # Larger size for better visibility
        "speed": 3,
        "target_pos": None,
        "dialogues": [],
        "interactable": False,
        "visible": True  # Explicit visibility flag
    },
    "Հայրիկ": {
        "pos": [240, 420],
        "size": (130, 180),
        "image_path": r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Hayrik.png",
        "dialogues": {
            "start": {
                "text": "Բարև ջան։ Ինչպե՞ս ե",
                "choices": [
                    {"text": "Բարև, լավ եմ։", "next": "good_response"},
                    {"text": "Հոգնած եմ...", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Ուրախ եմ լսել դա։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "tired_response": {
                "text": "Հանգստացիր մի քիչ։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "remember_good": {
                "text": "Այնտեղի լիճը զարմանալի էր։ Հիշու՞մ ես նավակով զբոսանքը։",
                "choices": [
                    {"text": "Այո, դա երբեք չեմ մոռանա։", "next": None},
                    {"text": "Մի քիչ, բայց շատ լավ էր։", "next": None}
                ]
            },
            "remember_none": {
                "text": "Շատ վատ։ Հաջորդ անգամ կփորձենք նոր հիշողություններ ստեղծել։",
                "choices": [
                    {"text": "Լավ գաղափար է։", "next": None},
                    {"text": "Միգուցե։", "next": None}
                ]
            }
        },
        "interactable": True,
        "visible": True
    },
    "Սամվել": {
       "pos": [85, 300],
        "size": (130, 180),
        "image_path": r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Samvel.png",
        "dialogues": {
            "start": {
                "text": "Բարև ջան։ Ինչպ",
                "choices": [
                    {"text": "Բարև, լավ եմ։", "next": "good_response"},
                    {"text": "Հոգնած եմ...", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Ուրախ եմ լսել դա։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "tired_response": {
                "text": "Հանգստացիր մի քիչ։ Հիշու՞մ ես մեր ամառանոցը...",
                "choices": [
                    {"text": "Այո, հիանալի էր։", "next": "remember_good"},
                    {"text": "Ոչ, չեմ հիշում։", "next": "remember_none"}
                ]
            },
            "remember_good": {
                "text": "Այնտեղի լիճը զարմանալի էր։ Հիշու՞մ ես նավակով զբոսանքը։",
                "choices": [
                    {"text": "Այո, դա երբեք չեմ մոռանա։", "next": None},
                    {"text": "Մի քիչ, բայց շատ լավ էր։", "next": None}
                ]
            },
            "remember_none": {
                "text": "Շատ վատ։ Հաջորդ անգամ կփորձենք նոր հիշողություններ ստեղծել։",
                "choices": [
                    {"text": "Լավ գաղափար է։", "next": None},
                    {"text": "Միգուցե։", "next": None}
                ]
            }
        },
        "interactable": True,
        "visible": True
    },
}