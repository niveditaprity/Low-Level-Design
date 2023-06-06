package observerdesignpattern;


import java.util.ArrayList;
import java.util.List;




interface Subscriber {
    public void update(String state);
}

class  Publisher {
    private List<Subscriber> subscribers = new ArrayList<>();
    private String state;

    public void subscribe(Subscriber s)
    {
        subscribers.add(s);
    }

    public  void unsubscribe(Subscriber s) {
        subscribers.remove(s);
    }

    public void notifyAllSubscribers() {
        for(Subscriber s: subscribers){
            s.update(state);
        }

    }

    public void setState(String state) {
        this.state = state;
        notifyAllSubscribers();
    }
}



class ConcreteSubscriber implements Subscriber {
    private String name;

    public ConcreteSubscriber(String name) {
        this.name = name;
    }

    public void update(String state) {
        System.out.println(name + " received state: " + state);
    }
}



public class MatchScore {
    public static void main(String[] args) {
        ConcreteSubscriber u1 = new ConcreteSubscriber("Nivedita");
        ConcreteSubscriber u2 = new ConcreteSubscriber("Surbhi");

        Publisher p = new Publisher();
        p.setState("India Won");
        p.subscribe(u1);
        p.subscribe(u2);
        p.notifyAllSubscribers();
        p.unsubscribe(u1);
        p.notifyAllSubscribers();


    }
}
