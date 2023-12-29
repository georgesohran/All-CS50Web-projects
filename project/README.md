# digGradeBook
### A digital grade book.
#### Video Demo:  <URL HERE>

## Technology
*This application is built using flask python framework, sqlite3 database, jinja2, html and alitle bit of JavaScript.*

## Registration.
Apon visiting the root directory you are being prompted to provide your name, password and type. The type field is where you should specify wether you are a teacher or a student. If not registered yet, you should visit regestration route by clicking the link on a navigation bar at the top of the screen.

If you try to register as a teacher you will be prompted to write the subject that you are teaching. If any of the steps go wrong you will receive a clear and understandable messege.

## As a student.
Now when you've successfully logged in as a student you can see the main page of the website. On the main page as a Student you can see the current schedule (and yes you now also study at sundays, you are welcome). Some of the cells on the table might be red, wich indicates that you have a below 4 grade for this subject and you shouldn't miss it.

Below the schedule you can see your current averege grades for all subjects. But if you want a more precise picture of your grades you should visit the grades page.

At your grades page you can see not only the averege of grades, but all grades you have ever got for each subject. And also you could check out the schedule page where you can just see the schedule without any distraction.

## As a teacher.
If you logged in as a teacher and correctly specified your subject, you should be able to see the main page. Here you can see the current schedule and when is the subjects that you teach. Also here you can see tha averege grade for each student you are teaching.

Now apon clicking the 'students' url on the navigation bar you will see the table displaing all their grades for your subject along with their averege grades. Here you can grade any one of them with any grade you want in the range from 1-5 (otherwise website is not going to update the table)

There also a schedule link you can click to see current schedule.

## Why gradebook?
I decided to make a gradebook, because our schools gradebook is somewhat bad and uncomfortable, so i just wanted to make a better gradebook.
## Story of making the website
Unfortunately, the deadlines are tight and i started building it 10 days ago. But 10 days ago i wanted to use django and htmx for this project. Only around 3-4 days later i realized that i won't be able to learn such a massive framework so quickly.

Then i switched to FastAPI and htmx, wich also appeard to be to difficult to learn in 7 days while building a website.Then i spent some time trying to adopt an ORM for this project such as SQLAlchemy, wich i found to be pretty frustrating, probobley because i had no time to properly learn it. So after all this 4-5 day strugle i finaly seteled pn flask and sqlite3. And i only had 5 or so days left to finish it before the new years eve.

The gradebook is still incomplete and lacking lots of features, like changing the schedule, deleting grades from a gradebook, an interactive chat with teachers, proper profile with email and pictures. I am going to continue working on this project, but now, as i'm typing these sentances i'm in a rush to wrap it all up, record a video and finish before January 1th 2024.

### Thank you for the course it left a huge impact on me and my career in tech. Thanks for everything CS50
