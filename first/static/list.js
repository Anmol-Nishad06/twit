const dots=document.querySelector('.threedot');
const dropdown=document.querySelector('.dropdown-content');

document.querySelectorAll('.fa-ellipsis-vertical').forEach(function(dot) {
    dot.addEventListener('click', function(e) {
        // Find the parent .username
        const usernameDiv = dot.closest('.username');
        // Toggle the show-dropdown class
        usernameDiv.classList.toggle('show-dropdown');
        // Hide dropdowns in other .username divs
        document.querySelectorAll('.username').forEach(function(otherDiv) {
            if (otherDiv !== usernameDiv) {
                otherDiv.classList.remove('show-dropdown');
            }
        });
        e.stopPropagation();
    });
});

// Hide dropdown when clicking outside
document.addEventListener('click', function() {
    document.querySelectorAll('.username').forEach(function(div) {
        div.classList.remove('show-dropdown');
    });
});

