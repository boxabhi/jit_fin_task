 <code>
    pip install requirements.txt
    <br>
    python manage.py runsever

    ##Live URL - https://jitfin.herokuapp.com/

 </code>

<hr>
<pre>
                <p>Task 1</p>
            <code >
               API for getting user info | <b>add query string username</b>   <span class="badge badge-primary">ACCEPTS GET REQUEST</span>
               <kbd >/get?username={YOUR USERNAME}</kbd>
            </code>
            </pre>

<hr>

<pre>
                <p>Task 2</p>
                <code class="">
                   API for getting followers of a user | <b>add query string username</b>   <span class="badge badge-primary">ACCEPTS GET REQUEST</span>
                   <kbd >/followers?username={YOUR USERNAME}</kbd>
                </code>
                </pre>

<hr>
<pre>
                <p>Task 3</p>
                <code class="">
                   API for getting highest followers of a user | <b>add query string username</b>   <span class="badge badge-primary">ACCEPTS GET REQUEST</span>
                   <kbd >/highest?username={YOUR USERNAME}</kbd>
                </code>
                </pre>


<hr>

<pre>
                <p>Task 4</p>
                <code >API for creating new repository for a user  <span class="badge badge-danger">ACCEPTS POST REQUEST</span>
                <kbd >/create/</kbd>
                You can get your token On your Github account:
                    go to Settings -> Developer Settings -> Personal Access Token Under OAuth Apps.
                    Now, Generate a New Access token
                <code>
                    {
                    "token" : "{YOUR TOKEN}" , 
                    "name" : "{REPO NAME YOU WANT TO CREATE}" 
                    }
             </code>
             </pre>

<hr>
<pre>
                <p>Task 5</p>
             <code >API for update description of a repository. <span class="badge badge-success">ACCEPTS PATCH REQUEST</span>
                <kbd >/update/</kbd>
                <code>
                    {
                    "token" : "{YOUR TOKEN}" , 
                    "name" : "{USERNAME}" ,
                    "repo" : "{REPO NAME}" ,
                    "owner" : "{OWNER NAME}" ,
                    "description" : "{DESCRIPTION}"
                    }
                </code>


<hr>




</div>