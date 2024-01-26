const {uploadPhoto} = require('./utils.js');
const {createUser} = require('./utils.js');

export default function handleProfileSignup() {   
  return Promise.all([uploadPhoto(), createUser()])
    .then((val) => {
      const {body} = val[0];
      const {firstName} = val[1];
      const {lastName} = val[1];
      console.log(body, firstName, lastName);
    })
    .catch(() => console.error('Signup system offline'));
}
