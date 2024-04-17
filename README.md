## Tasks

1. Create a new model called Genre with a single field called “name”. Add the following records to
the Genre model: (Action, Adventure, Animated, Comedy, Drama, Fantasy, Horror, RomCom) (5)

2. Extend the Movie model by including the Genre model as a “ManyToManyField”. (5)

3. Create additional views for creating and updating Movie information. Please ensure that you utilise Django forms
for this and ensure that multiple genres can be selected for a movie. (15)

4. Create a login page for the site and set the route for this so that it loads as the site’s homepage (root).
Utilise the default Django user model for authentication. A single user (admin) currently exists. (10)

5. Upon successful login, the application should redirect to the Movie list view. The list view, detail view,
create view and update view should only be accessible when logged in. (5)

6. Add a navbar to the base template with links to the existing views and the new views you have created. Ensure
that the links only appear once logged in. We are expecting you to utilise Bootstrap when styling the navbar. 
 (10)

Please note that you will be graded on your ability to suitably complete the task as well as your presentation and styling.
