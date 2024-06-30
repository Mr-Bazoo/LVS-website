document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/students')
        .then(response => response.json())
        .then(students => {
            const studentList = document.getElementById('student-list');
            students.forEach(student => {
                const studentElement = document.createElement('div');
                studentElement.innerHTML = `
                    <img src="${student.avatar}" alt="${student.name}" width="50">
                    <span>${student.name}</span>
                `;
                studentList.appendChild(studentElement);
            });
        });
});