// Modal functions
function openModal() {
    document.getElementById('addWineModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('addWineModal').style.display = 'none';
    document.getElementById('wineForm').reset();
    // Reset range value displays
    document.getElementById('tanninValue').textContent = '5';
    document.getElementById('sweetnessValue').textContent = '5';
    document.getElementById('appealValue').textContent = '5';
}

// Range slider value updates
function updateTanninValue(value) {
    document.getElementById('tanninValue').textContent = value;
}

function updateSweetnessValue(value) {
    document.getElementById('sweetnessValue').textContent = value;
}

function updateAppealValue(value) {
    document.getElementById('appealValue').textContent = value;
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('addWineModal');
    if (event.target === modal) {
        closeModal();
    }
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});
