import pygame
import sys
import random
import math
import os
import subprocess


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basement Adventure - Ընտրություններով")

# Colors
BLACK = (15, 20, 25)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
HIGHLIGHT = (200, 200, 0)

# Font
try:
    font_path = r"C:\Users\ARMAN\Downloads\game1\Noto_Sans_Armenian\NotoSansArmenian-VariableFont_wdth,wght.ttf"
    font = pygame.font.Font(font_path, 24)
except:
    font = pygame.font.SysFont("Arial", 24)

# Load background image
try:
    bg_path = r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_BG.png"
    background_img = pygame.image.load(bg_path).convert()
    background_img = pygame.transform.scale(background_img, (800, 600))
except Exception as e:
    print(f"Failed to load background image: {e}")
    background_img = None

# Characters dictionary (use your full version — this is shortened)
import pygame
import sys
import os
import random
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basement Adventure - Ընտրություններով")

# Colors
BLACK = (15, 20, 25)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
HIGHLIGHT = (200, 200, 0)

# Font
try:
    font_path = r"C:\Users\ARMAN\Downloads\game1\Noto_Sans_Armenian\NotoSansArmenian-VariableFont_wdth,wght.ttf"
    font = pygame.font.Font(font_path, 24)
except:
    font = pygame.font.SysFont("Arial", 24)

# Load background image
try:
    bg_path = r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_BG.png"
    background_img = pygame.image.load(bg_path).convert()
    background_img = pygame.transform.scale(background_img, (800, 600))
except Exception as e:
    print(f"Failed to load background image: {e}")
    background_img = None

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
                    {"text": "Սարսափելի է", "next": None},
                    {"text": "ավելի լավ է, բաժանվես ու պարտքերդ մարես", "next": None}
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
                "choices": [
                    {"text": "Հայրի՜կ", "next": None},
                ]
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
                "text": "Բարև փոքրիկ։ Ինչպե՞ս ես։",
                "choices": [
                    {"text": "Բարև, լավ եմ։", "next": "good_response"},
                    {"text": "Հոգնած եմ...", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Բուսակերությունը լավ բան է, փորձել ես երբևէ՞։",
                "choices": [
                    {"text": "Այո իհարկե, բայց էլ չեմ փորձի", "next": None},
                    {"text": "Ոչ, կմտածեմ", "next": None}
                ]
            },
            "tired_response": {
                "text": "Ինչու ինչ է պատահել՞",
                "choices": [
                    {"text": "Ոչինչ, մի քիչ նստեմ կանցնի", "next": None},
                    {"text": "Կառոբկա Աշոտի մոտ այսօր, ոչինչ չես նկատում", "next": None}
                ]
            },
        },
        "interactable": True,
        "visible": True
    },
    "Տիգրան": {
    
        "pos": [340, 340],
        "size": (130, 180),
        "image_path": r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Tigran.png",
        "dialogues": {
            "start": {
                "text": "Էս թերթերին որ լսես, կպարզվի ազգի դավաճան ենք",
                "choices": [
                    {"text": "Ովքե՞ր, մե՞նք", "next": "good_response"},
                ]
            },
            "good_response": {
                "text": "դու դեռ փոքր ես, սրանք էլ բան չեն հասկանում",
                "choices": [
                    {"text": "Իսկ ի՞նչ պիտի հասկանան", "next": "remember_good"},
                    {"text": "ասա կհասկանամ", "next": "remember_none"}
                ]
            },
            "remember_none": {
                "text": "ասելու բան չկա, նայիր սրանց ինչ եմ անելու․․․",
                "choices": [
                    {"text": "Ու՞ր ես գնում", "next": None},
                ]
            },
            "remember_good": {
                "text": "ուշ է արդեն հասանալու համար, ստիպված են այսպես ապրել",
                "choices": [
                    {"text": "Ափսոս", "next": None},
                    {"text": "դե ինչ արած․․․", "next": None}
                ]
            },
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
                "text": "Տղաս, ուզու՞մ ես գնանք քայլենք այսօր",
                "choices": [
                    {"text": "Այո, անպայման", "next": "good_response"},
                    {"text": "Գործերդ շատ են այսօր, թող ման ուրիշ անգամ", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Դե մի փոքր սպասիր, էտ անիծվածին պիտի հանեմ նկարից, հետո կգնանք",
                "choices": [
                    {"text": "Հա, Աշոտն էլ էր դրա մասին խոսում", "next": None},
                    {"text": "Բայց, լավ էլ նկար է, ինչի՞ եք ձեռք տալիս", "next": None}
                ]
            },
            "tired_response": {
                "text": "Ճի՛շտ ես, դե գնամ նկար փորձեմ ետ վերցնել դրանից, չեմ թողնի գողանա",
                "choices": [
                    {"text": "Լավ, հայրիկ, չեմ խանգարի", "next": None},
                    {"text": "նկարը ո՞նց պիտի գողանան", "next":None }
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
                "text": "Բարև տղաս։ Ինչպե՞ս ես։",
                "choices": [
                    {"text": "Բարև, լավ եմ, էլի աշխատո՞ւմ ես, Կարելի՞ է նայել", "next": "good_response"},
                    {"text": "Բարև, լավ, Աշոտը այսօր մի տեսակ է", "next": "tired_response"}
                ]
            },
            "good_response": {
                "text": "Իհարկե, քո ընկերակցությունը ավելի գերադասելի է քան սրանցը",
                "choices": [
                    {"text": "Շնորհակալություն", "next": None},
                    {"text": "Հիմա կգամ", "next": None}
                ]
            },
            "tired_response": {
                "text": "Աշոտն է էլի, երևի էլի նոր գաղափար ունի",
                "choices": [
                    {"text": "Հնարավոր է", "next": None},
                    {"text": "չէ, այսօր յուրօինակ է իրեն պահում", "next": None}
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

# Load images
for name, char in characters.items():
    if "image_path" in char:
        try:
            img = pygame.image.load(char["image_path"]).convert_alpha()
            img = pygame.transform.scale(img, char["size"])
            char["image"] = img
        except Exception as e:
            print(f"Failed to load image for {name}: {e}")
            char["image"] = None
    else:
        char["image"] = None

# Game state
current_character = None
current_node_key = "start"
selected_choice = 0
show_choices = False
insanity_effect = False
clicked_character_name = None

def draw_basement():
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(BLACK)

def draw_characters():
    for name, char in characters.items():
        if char["visible"]:
            if char["image"]:
                screen.blit(char["image"], char["pos"])
            else:
                pygame.draw.rect(screen, GRAY, (*char["pos"], *char["size"]))
            name_text = font.render(name, True, WHITE)
            screen.blit(name_text, (char["pos"][0], char["pos"][1] - 30))

def draw_dialogue():
    if not current_character:
        return

    dialogue = characters[current_character]["dialogues"][current_node_key]
    wrapped_text = []
    words = dialogue['text'].split()
    line = ""
    for word in words:
        test_line = line + word + " "
        if font.size(test_line)[0] > 600:
            wrapped_text.append(line.strip())
            line = word + " "
        else:
            line = test_line
    wrapped_text.append(line.strip())

    # Draw semi-transparent box a bit higher
    box_top = 420
    text_height = 24 * (len(wrapped_text) + 1 + 2 * len(dialogue.get("choices", [])))
    dialogue_rect = pygame.Surface((700, text_height + 20), pygame.SRCALPHA)
    dialogue_rect.fill((0, 0, 0, 180))
    screen.blit(dialogue_rect, (50, box_top))

    # Draw character name and dialogue
    for i, line in enumerate(wrapped_text):
        text_surf = font.render(f"{current_character}: {line}" if i == 0 else line, True, WHITE)
        screen.blit(text_surf, (60, box_top + 10 + i * 24))

    # Draw choices
    if show_choices:
        base_y = box_top + 10 + len(wrapped_text) * 24 + 10
        for i, choice in enumerate(dialogue["choices"]):
            wrapped_lines = []
            words = choice['text'].split()
            line = ""
            for word in words:
                test_line = line + word + " "
                if font.size(test_line)[0] > 600:
                    wrapped_lines.append(line.strip())
                    line = word + " "
                else:
                    line = test_line
            wrapped_lines.append(line.strip())

            for j, line in enumerate(wrapped_lines):
                color = HIGHLIGHT if i == selected_choice and j == 0 else WHITE
                choice_surf = font.render(line.strip(), True, color)
                screen.blit(choice_surf, (70, base_y + i * 50 + j * 24))

def is_click_on_character(pos, character):
    if not character["visible"] or not character["interactable"]:
        return False
    x, y = character["pos"]
    w, h = character["size"]
    return x <= pos[0] <= x + w and y <= pos[1] <= y + h

def move_toward_target(grig, target_pos):
    if target_pos is None:
        return False
    dx = target_pos[0] - grig["pos"][0]
    dy = target_pos[1] - grig["pos"][1]
    distance = math.hypot(dx, dy)
    if distance < grig["speed"]:
        grig["pos"] = list(target_pos)
        return True
    grig["pos"][0] += grig["speed"] * dx / distance
    grig["pos"][1] += grig["speed"] * dy / distance
    return False

def main():
    global current_character, current_node_key, selected_choice, show_choices, insanity_effect, clicked_character_name
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for name, char in characters.items():
                    if is_click_on_character(event.pos, char):
                        clicked_character_name = name
                        cx, cy = char["pos"]
                        cw, ch = char["size"]
                        if name == "Սամվել":
                            characters["Գրիգ"]["target_pos"] = [cx + cw + 10, cy + 50]
                        else:
                            characters["Գրիգ"]["target_pos"] = [cx - 70, cy + 50]
                        current_character = None
                        show_choices = False
                        break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if show_choices and current_character:
                        choice = characters[current_character]["dialogues"][current_node_key]["choices"][selected_choice]
                        next_node = choice["next"]
                        if next_node is None:
                            # Աշոտ remember_none event
                            if current_character == "Կառոբկա Աշոտ" and current_node_key == "remember_none":
                                try:
                                    new_path = r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Ashot_Angry.png"
                                    new_img = pygame.image.load(new_path).convert_alpha()
                                    new_img = pygame.transform.scale(new_img, characters["Կառոբկա Աշոտ"]["size"])
                                    characters["Կառոբկա Աշոտ"]["image"] = new_img
                                except Exception as e:
                                    print(f"Failed to load angry image for Աշոտ: {e}")
                                for _ in range(10):
                                    draw_basement()
                                    draw_characters()
                                for _ in range(20):
                                    x, y = random.randint(0, 800), random.randint(0, 600)
                                    pygame.draw.line(screen, RED, (x, y), (x + random.randint(5, 20), y + random.randint(5, 20)), 2)
                                    pygame.display.flip()
                                    pygame.time.delay(10)
                                    if random.random() < 0.3:
                                        flicker = pygame.Surface((800, 600))
                                        flicker.fill((220, 220, 255))
                                        flicker.set_alpha(random.randint(30, 100))
                                        screen.blit(flicker, (0, 0))

                                    pygame.display.flip()
                                    pygame.time.delay(50)
                                # Fade out
                                for alpha in range(0, 255, 5):
                                    fade_surface = pygame.Surface((800, 600))
                                    fade_surface.fill((0, 0, 0))
                                    fade_surface.set_alpha(alpha)
                                    draw_basement()
                                    draw_characters()
                                    screen.blit(fade_surface, (0, 0))
                                    pygame.display.flip()
                                    pygame.time.delay(30)

                                pygame.time.delay(1000)
                                screen.fill((0, 0, 0))
                                message = font.render("Աշոտին ես այլևս չտեսա, ու իմ մոտ իր մասին էլ չէին խոսում։", True, WHITE)
                                screen.blit(message, (screen.get_width() // 2 - message.get_width() // 2,
                                                    screen.get_height() // 2 - message.get_height() // 2))
                                pygame.display.flip()
                                pygame.time.delay(4000)
                                pygame.quit()
                                sys.exit()

                            # Տիգրան remember_none event
                            elif current_character == "Տիգրան" and current_node_key == "remember_none":
                                try:
                                    samvel_path = r"C:\Users\ARMAN\Downloads\game1\Characters\Nkux_Samvel_NoPC.png"
                                    samvel_img = pygame.image.load(samvel_path).convert_alpha()
                                    samvel_img = pygame.transform.scale(samvel_img, characters["Սամվել"]["size"])
                                    characters["Սամվել"]["image"] = samvel_img
                                except Exception as e:
                                    print(f"Failed to load Samvel NoPC image: {e}")

                                characters["Տիգրան"]["visible"] = False

                            current_character = None


                        else:
                            current_node_key = next_node
                        show_choices = False
                    elif current_character:
                        node = characters[current_character]["dialogues"][current_node_key]
                        if node["choices"]:
                            show_choices = True
                            selected_choice = 0
                elif event.key == pygame.K_DOWN and show_choices:
                    selected_choice = min(selected_choice + 1,
                        len(characters[current_character]["dialogues"][current_node_key]["choices"]) - 1)
                elif event.key == pygame.K_UP and show_choices:
                    selected_choice = max(selected_choice - 1, 0)
                elif event.key == pygame.K_i:
                    insanity_effect = not insanity_effect

        grig = characters["Գրիգ"]
        if grig["target_pos"]:
            reached = move_toward_target(grig, grig["target_pos"])
            if reached:
                grig["target_pos"] = None
                if clicked_character_name:
                    current_character = clicked_character_name
                    current_node_key = "start"
                    show_choices = False
                    clicked_character_name = None

        draw_basement()
        draw_characters()
        draw_dialogue()

        if insanity_effect and current_character == "Կառոբկա Աշոտ":
            for _ in range(10):
                x, y = random.randint(0, 800), random.randint(0, 600)
                pygame.draw.line(screen, RED, (x, y), (x + random.randint(5, 20), y + random.randint(5, 20)), 1)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    for char in characters.values():
        char["visible"] = True
    main()
    pygame.quit()
    sys.exit()


# Load images
for name, char in characters.items():
    if "image_path" in char:
        try:
            img = pygame.image.load(char["image_path"]).convert_alpha()
            img = pygame.transform.scale(img, char["size"])
            char["image"] = img
        except Exception as e:
            print(f"Failed to load image for {name}: {e}")
            char["image"] = None
    else:
        char["image"] = None

# Game state
current_character = None
current_node_key = "start"
selected_choice = 0
show_choices = False
insanity_effect = False
clicked_character_name = None

def draw_basement():
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(BLACK)

def draw_characters():
    for name, char in characters.items():
        if char["visible"]:
            if char["image"]:
                screen.blit(char["image"], char["pos"])
            else:
                pygame.draw.rect(screen, GRAY, (*char["pos"], *char["size"]))
            name_text = font.render(name, True, WHITE)
            screen.blit(name_text, (char["pos"][0], char["pos"][1] - 30))

def draw_dialogue():
    if not current_character:
        return

    dialogue = characters[current_character]["dialogues"][current_node_key]
    wrapped_text = []
    words = dialogue['text'].split()
    line = ""
    for word in words:
        test_line = line + word + " "
        if font.size(test_line)[0] > 600:
            wrapped_text.append(line.strip())
            line = word + " "
        else:
            line = test_line
    wrapped_text.append(line.strip())

    # Draw semi-transparent box
    text_height = 24 * (len(wrapped_text) + 1 + 2 * len(dialogue.get("choices", [])))
    dialogue_rect = pygame.Surface((700, text_height + 20), pygame.SRCALPHA)
    dialogue_rect.fill((0, 0, 0, 180))
    screen.blit(dialogue_rect, (50, 480))

    # Draw character name and dialogue
    for i, line in enumerate(wrapped_text):
        text_surf = font.render(f"{current_character}: {line}" if i == 0 else line, True, WHITE)
        screen.blit(text_surf, (60, 490 + i * 24))

    # Draw choices
    if show_choices:
        base_y = 490 + len(wrapped_text) * 24 + 10
        for i, choice in enumerate(dialogue["choices"]):
            wrapped_lines = []
            words = choice['text'].split()
            line = ""
            for word in words:
                test_line = line + word + " "
                if font.size(test_line)[0] > 600:
                    wrapped_lines.append(line.strip())
                    line = word + " "
                else:
                    line = test_line
            wrapped_lines.append(line.strip())

            for j, line in enumerate(wrapped_lines):
                color = HIGHLIGHT if i == selected_choice and j == 0 else WHITE
                choice_surf = font.render(line, True, color)
                screen.blit(choice_surf, (70, base_y + i * 50 + j * 24))
                color = HIGHLIGHT if i == selected_choice and j == 0 else WHITE
                choice_surf = font.render(line.strip(), True, color)
                screen.blit(choice_surf, (150, 530 + (i * 50) + (j * 24)))

def is_click_on_character(pos, character):
    if not character["visible"] or not character["interactable"]:
        return False
    x, y = character["pos"]
    w, h = character["size"]
    return x <= pos[0] <= x + w and y <= pos[1] <= y + h

def move_toward_target(grig, target_pos):
    if target_pos is None:
        return False
    dx = target_pos[0] - grig["pos"][0]
    dy = target_pos[1] - grig["pos"][1]
    distance = math.hypot(dx, dy)
    if distance < grig["speed"]:
        grig["pos"] = list(target_pos)
        return True
    grig["pos"][0] += grig["speed"] * dx / distance
    grig["pos"][1] += grig["speed"] * dy / distance
    return False

def main():
    global current_character, current_node_key, selected_choice, show_choices, insanity_effect, clicked_character_name
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for name, char in characters.items():
                    if is_click_on_character(event.pos, char):
                        clicked_character_name = name
                        cx, cy = char["pos"]
                        cw, ch = char["size"]
                        if name == "Սամվել":
                            characters["Գրիգ"]["target_pos"] = [cx + cw + 10, cy + 50]
                        else:
                            characters["Գրիգ"]["target_pos"] = [cx - 70, cy + 50]
                        current_character = None
                        show_choices = False
                        break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if show_choices and current_character:
                        choice = characters[current_character]["dialogues"][current_node_key]["choices"][selected_choice]
                        next_node = choice["next"]
                        if next_node is None:
                            current_character = None
                        else:
                            current_node_key = next_node
                        show_choices = False
                    elif current_character:
                        node = characters[current_character]["dialogues"][current_node_key]
                        if node["choices"]:
                            show_choices = True
                            selected_choice = 0
                elif event.key == pygame.K_DOWN and show_choices:
                    selected_choice = min(selected_choice + 1,
                        len(characters[current_character]["dialogues"][current_node_key]["choices"]) - 1)
                elif event.key == pygame.K_UP and show_choices:
                    selected_choice = max(selected_choice - 1, 0)
                elif event.key == pygame.K_i:
                    insanity_effect = not insanity_effect

        grig = characters["Գրիգ"]
        if grig["target_pos"]:
            reached = move_toward_target(grig, grig["target_pos"])
            if reached:
                grig["target_pos"] = None
                if clicked_character_name:
                    current_character = clicked_character_name
                    current_node_key = "start"
                    show_choices = False
                    clicked_character_name = None

        draw_basement()
        draw_characters()
        draw_dialogue()

        if insanity_effect and current_character == "Կառոբկա Աշոտ":
            for _ in range(10):
                x, y = random.randint(0, 800), random.randint(0, 600)
                pygame.draw.line(screen, RED, (x, y), (x + random.randint(5, 20), y + random.randint(5, 20)), 1)

        pygame.display.flip()
        clock.tick(60)

def auto_build_exe():
    script_name = os.path.basename(__file__)
    exe_name = os.path.splitext(script_name)[0] + '.exe'
    
    # Don't rebuild if we're already running the exe
    if getattr(sys, 'frozen', False):
        return

    # Skip if exe already exists
    if os.path.exists(exe_name):
        return

    print("Building .exe from script...")
    subprocess.call([
        'pyinstaller',
        '--onefile',
        '--noconfirm',
        script_name
    ])
    print(f"Executable created: dist/{exe_name}")
    sys.exit(0)

auto_build_exe()

if __name__ == "__main__":
    for char in characters.values():
        char["visible"] = True
    main()
    pygame.quit()
    sys.exit()


