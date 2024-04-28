# process
   1. creation of idea - co pleted 4/28/2024
   2. Visual Design of application
   3. Database / data
   4. Creation of project


# 4/28/2024

Today we will be focusing on making the base idea of the project and having the necessary tools. First, let's look at our current hobbies:

* Hiking - various apps already display hiking trails, and provide the basic info so what is the point of reinventing the wheel
* Marine Biology/zoology - This can open a lot of different things as this is broad, we could have an application that helps zoologists in some way. 
* Fishing - Here is where we can find different types of apps as we have fish tournaments, an Inventory system, library of the different fish species which includes information on how to find, and catch them, habitat, description, natural prey, and handling tips


## Project:
Well after some time, it has come to my attention that the US tries to make endangered species an important topic however we need to find a way to make an interactive way to get children and young adults to learn more about these species

### Details 
So now that we have the idea #1: Endangered Species navigator

How to go forward with this:
1. We would like to construct this in Python, we would like a visual web application that allows children and young adults to see visual representations of these creatures with facts and news of these creatures.
 
2. As the topic of Endangered Species is one that tends to be covered a lot through documentation, the best way to attract attention toward conservation is not through lectures but through interactive visuals similar to the concept of zoos. Think about it, Zoos convince many of conservation due to the physical appeal of said creatures so how about a way to amplify that aspect through a similar approach with endangered species on a virtual approach as these creatures are very few?

#### User Flow

* When the user enters the site they should easily select an animal they would like to learn about, we can have filters for example mammals, insects, birds, Aquatic
* There is no need for the user to log in to the site, as there is no benefit to doing so. The main thing is for this web application to easily allow the user to click a box of the designated animal. By default, it will be sorted by alphabetical order
* The design should be simple, one simple click should lead them to exactly where it is

#### Wireframing
```
           +-------------+
          | Main Page   |
          +-------------+
                |
          +-------------+
          | Animal Page |
          +-------------+
             /          \
            /            \
   +----------------+   +-------------------+
   | Timeline       |   | Interactive       |
   |                |   | Display           |
   +----------------+   +-------------------+
```

#### Design System 

UI design journey, we need to use a guideline for colors, fonts, and icons (Real-time colors can help us with this process)

1. We need a color that represents Endangered species, and we need to ensure the background and text. primary, secondary, accent, error, and success color to reflect the project
 
2. We need a concise and easy-to-read font for everyone, typescale can help with determining the font size and ratios. This is so we have a Title, body, and small text
 * Title 32 px bold
 * Body 18px regular/Bold
 * small 14px regular
 
3. icons which we can acquire from Figma
 
4. Input buttons, category inputs, and website cards
 
#### Visual Approach

Let's start with the visual design of the application:
 * Visual hierarchy
 * Contrast
 * Balance
 * Consistency
 * Simplicity
 * Feedback 


#### Database
#### Database
We will be utilizing PostgreSQL to hold a database of all endangered species, there is currently a dataset of endangered species that should hold information that can be extracted that will allow us to create tables and schema for us to construct it. 

* SPECIES TABLE
 1. ID
 2. NAME
 3. TYPE
 4. HABITAT
 5. LIFECYCLE
 6. FOOD 
   




