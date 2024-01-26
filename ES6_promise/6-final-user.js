const signUpUser = require('./4-user-promise.js').default;
const uploadPhoto = require('./5-photo-reject.js').default;

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userRes = signUpUser(firstName, lastName)
    .then((res) => ({
        status: 'fulfilled',
        value: res,
    }))
    .catch((err) => ({
      status: 'rejected',
      value: err,    
    }));
    const photoRes = uploadPhoto(fileName)
    .then((res) => ({
        status: 'fulfilled',
        value: res,
    }))
    .catch((err) => ({
      status: 'rejected',
      value: err,    
    }));
    const arrayPromises = [userRes, photoRes];
    return Promise.allSettled(arrayPromises);
}
