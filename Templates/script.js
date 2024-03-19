console.log('Starting')
var qualifyBtn = document.getElementById('qualifybtn');
var qualifyDiv = document.getElementById('qualify');
qualifyBtn.addEventListener('click', function() {
    // Remove the 'closedpop' class from the div
    qualifyDiv.classList.remove('closedpop');
});

var SignInPopup = document.getElementById('signIn');
var SignInBtn = document.getElementById('signInbtn');
SignInBtn.addEventListener('click', function() {
    SignInPopup.classList.remove('closedpop');
});

var SignUpPopup = document.getElementById('signUp');
var signUpbtn = document.getElementById('signUpbtn');
signUpbtn.addEventListener('click', function() {
  SignUpPopup.classList.remove('closedpop');
});

closeBtn = document.querySelectorAll('.closepopup')
console.log(closeBtn)
closeBtn.forEach(function(clickedcloseBtn){
  clickedcloseBtn.addEventListener('click', function() {
  var popups = document.querySelectorAll('.pop');
  popups.forEach(function(popup) {
    popup.classList.add('closedpop');
    console.log(popup)
    console.log('closed')
  });
})})

confirmSignInbtn = document.getElementById('confirmSignInbtn')
confirmSignInbtn.addEventListener('click', async function () {
  // sign in a user
  const signInEmail = document.getElementById('signinemail')
  const SignInPassword = document.getElementById('SignInPassword')
  const email = signInEmail.value;
  const password = SignInPassword.value;

  try {
    const response = await fetch('/confirm_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
    });

    const data = await response.json();

    // Handle the response data
    console.log(data);

    // Example: Check for a valid response before updating the UI
    if (data && typeof data === 'object' && !('error' in data)) {
        console.log('Welcome!!!');
        console.log('First Name:', data['First Name']);
        console.log('Last Name:', data['Last Name']);
        console.log('Email:', data['Email']);
        console.log('City:', data['City']);

        displayName.textContent = `${data['First Name']} ${data['Last Name']}`;
        displayEmail.textContent = data['Email'];
        displayLocation.textContent = data['City'];

        const formattedDateTime = convertTimestampToDateTime(data['Last Time Played']);

        displayTimer.textContent = (formattedDateTime.time) + ", " + formattedDateTime.date;
        generateAvatar(data['First Name'], data['Last Name'])

        UserSignedIn = true;
        closePopups();
    } else {
        // Handle invalid response or error
        console.log('Invalid response or error:', data);
    }
  } catch (error) {
      console.error('Error:', error);
  }

});

confirmSignUpbtn = document.getElementById('signUpbtn')
confirmSignInbtn.addEventListener('click', async function () {
  // sign in a user
  const signInEmail = document.getElementById('signinemail')
  const SignInPassword = document.getElementById('SignInPassword')
  const email = signInEmail.value;
  const password = SignInPassword.value;

});



function sendData() {
  const request = "Hello World";
  console.log("got into sendData", request)
  fetch('http://localhost:5000/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ data: request })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // Do something with the response data if needed
            })
            .catch((error) => {
                console.error('Error:', error);
            });

}