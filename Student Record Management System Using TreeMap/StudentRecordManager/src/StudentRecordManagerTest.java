import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class StudentRecordManagerTest {
    private StudentRecordManager manager;
    @org.junit.jupiter.api.BeforeEach
    void setUp() {

        manager = new StudentRecordManager();
        manager.addStudent(101,"Alice Wonderland", 3.5);
        manager.addStudent(102,"George Bush", 3.1);
        manager.addStudent(103,"Jackie Chan", 3.0);
        manager.addStudent(104,"Michael Jackson", 3.2);
        manager.addStudent(105,"Bob Voss", 3.0);
    }

    @org.junit.jupiter.api.Test
    void addStudent() {
        assertTrue(manager.addStudent(106,"Mary Sue", 4.0));
    }

    @org.junit.jupiter.api.Test
    void deleteStudent() {
        assertTrue(manager.deleteStudent(102));
    }

    @org.junit.jupiter.api.Test
    void updateStudentGpa() {
        assertTrue(manager.updateStudentGpa(101,3.4));
    }

    @org.junit.jupiter.api.Test
    void findStudentHigherThanSpecifiedValue() {
        assertDoesNotThrow(() -> manager.findStudentHigherThanSpecifiedValue(3.0));
    }

    @org.junit.jupiter.api.Test
    void displayAllRecord(){
        assertDoesNotThrow(()-> manager.displayAllRecord());
    }
}