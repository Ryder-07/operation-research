import math

def exp_queue_size(lambd,mu):
    rho = lambd/mu
    print(rho)
    exp_size = rho/ (1 - rho )
    return exp_size

def queue_size_prob (lambd,mu,queue_size):
    rho = lambd/mu
    if rho>=1:
        print("rho must be less than 1")
    return ((rho**queue_size))


arrivals_per_day=30
interarrival_time_avg=1/(arrivals_per_day/24)
service_time_avg=36/60
lambd=1/interarrival_time_avg
mu=1/service_time_avg
expected_size = exp_queue_size(lambd,mu)

print("expected queue size = ",round(expected_size,2),"trains")

queue_size=10
queue_prob= queue_size_prob(lambd,mu,queue_size)
print("the probability of exceeding queue size is",round(queue_prob,2))
new_arrivals_per_day=33
new_interarrival_time_avg=1/(arrivals_per_day/24)
lambd=1/new_interarrival_time_avg
lambd=11/480
mu=1/36
new_expected_size = exp_queue_size(lambd,mu)
print("expected queue size with ",new_arrivals_per_day,"arrivals per day is ",round(new_expected_size,2),"trains")
new_queue_prob= queue_size_prob(lambd,mu,queue_size)
print("probability of queue size exceeding ",queue_size,"arrivals per day is",round(new_queue_prob,2))

