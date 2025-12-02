package exam_prep;

public class Student extends UniversityMember implements LabAccess {
    private double gpa;

    public Student(String id, String name, double gpa){
        super(id,name); //passes id/name to parent
        this.gpa = gpa;

    }
    @Override 
    public String getRole() {
        return "Student";
    }
    public boolean canLogin(){
        if (this.gpa > 1.0) {
            return true;
        }
        return false;
    }
    public int getPrintQuota(){
        return 50;
    }
}
