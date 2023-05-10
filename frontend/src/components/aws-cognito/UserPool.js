import { CognitoUserPool } from "amazon-cognito-identity-js";

const userPoolId = process.env.REACT_APP_USER_POOL_ID;
const clientId = process.env.REACT_APP_USER_POOL_CLIENT_ID;
const poolData = {
  UserPoolId: userPoolId,
  ClientId: clientId,
};

const userPool = new CognitoUserPool(poolData);
export default userPool;
