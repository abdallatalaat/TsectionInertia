import os

cmd = 'mode 40,40'
os.system(cmd)

input_msgs = ["ts: ", "t: ", "b: ", "B: ", ]

while True:
    valid = True
    try:
        print("\nUSE THE SAME INPUT UNITS")
        inputs = [input("enter "+ i) for i in input_msgs]
        ts, t, b, B = [float(i) for i in inputs]

    except:
        print("INVALID INPUT")
        valid = False

    if valid:
        alpha = ts/t
        beta = b/B

        mu = (((alpha**3+beta*(1-alpha)**3)/12)
                       +alpha*(1-0.5*alpha-((alpha*(1-0.5*alpha)+0.5*beta*(1-alpha)**2)/(alpha+beta*(1-alpha))))**2
                       +beta*(1-alpha)*(0.5-0.5*alpha-((alpha*(1-0.5*alpha)+0.5*beta*(1-alpha)**2)/(alpha+beta*(1-alpha))))**2)

        I = mu * B * t**3
        print("\nmu = ",int(mu*10000))
        print("I (input units) = {:e} \n----------------------------\n".format(I))
