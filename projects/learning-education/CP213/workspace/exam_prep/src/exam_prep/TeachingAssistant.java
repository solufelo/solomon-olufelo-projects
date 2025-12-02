package exam_prep;

public class TeachingAssistant extends Student {
    
    public TeachingAssistant(String id, String name, double gpa){
        super(id,name,gpa);

    }
    @Override
    public int getPrintQuota(){
        return 200;
    }
    public String getRole() {
        return "TA";
    }
}
