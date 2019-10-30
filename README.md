# volcano
Baller team with the baller backend -- Volcano is the powerhouse for FindFlix


IN order to run:
ssh -i "lavalab-f2019.pem" ubuntu@ec2-3-233-182-74.compute-1.amazonaws.com

Routes:

ec2-3-233-182-74.compute-1.amazonaws.com:5000/

- phoneSignup --> will add a phone to a database


Testing procs:
curl -d "param1=value1&param2=value2" -X POST http://ec2-3-233-182-74.compute-1.amazonaws.com:5000/
