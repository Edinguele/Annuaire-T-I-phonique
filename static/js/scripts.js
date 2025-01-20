document.getElementById('openAddForm').onclick = function () {
    document.getElementById('addContactForm').style.display = 'block';
}

document.getElementById('closeAddForm').onclick = function () {
    document.getElementById('addContactForm').style.display = 'none';
}

document.getElementById('closeEditForm').onclick = function () {
    document.getElementById('editContactForm').style.display = 'none';
}
document.querySelectorAll('.editButton').forEach(button => {
    button.onclick = function () {
        const contactId = this.getAttribute('data-id');
        const contactNom = this.getAttribute('data-nom');
        const contactPrenom = this.getAttribute('data-prenom');
        const contactTelephone = this.getAttribute('data-telephone');
        const contactPoste = this.getAttribute('data-poste');
        const contactAgence = this.getAttribute('data-agence');

        document.getElementById('editContactId').value = contactId;
        document.getElementById('editNom').value = contactNom;
        document.getElementById('editPrenom').value = contactPrenom;
        document.getElementById('editTelephone').value = contactTelephone;
        document.getElementById('editPoste').value = contactPoste;
        document.getElementById('editAgence').value = contactAgence;

        document.getElementById('editContactForm').style.display = 'block';
    }
});

document.getElementById('searchInput').addEventListener('keyup', function () {
    const searchText = this.value.toLowerCase();
    const filterType = document.getElementById('filterType').value;
    const rows = document.querySelectorAll('#contactsTable tbody tr');

    rows.forEach(row => {
        let text = '';
        if (filterType === 'all') {
            text = row.textContent.toLowerCase();
        } else {
            const index = {
                'nom': 0,
                'prenom': 1,
                'poste': 3,
                'agence': 4
            }[filterType];
            text = row.cells[index].textContent.toLowerCase();
        }
        row.style.display = text.includes(searchText) ? '' : 'none';
    });
});
document.getElementById('searchInput').addEventListener('keyup', function () {
    const searchText = this.value.toLowerCase();
    const filterType = document.getElementById('filterType').value;
    const rows = document.querySelectorAll('#contactsTable tbody tr');

    rows.forEach(row => {
        let text = '';
        if (filterType === 'all') {
            text = row.textContent.toLowerCase();
        } else {
            const index = {
                'nom': 0,
                'prenom': 1,
                'poste': 3,
                'agence': 4
            }[filterType];
            text = row.cells[index].textContent.toLowerCase();
        }
        row.style.display = text.includes(searchText) ? '' : 'none';
    });
});

document.querySelectorAll('.sortable').forEach(header => {
    header.addEventListener('click', function () {
        const column = this.dataset.column;
        const tbody = document.querySelector('#contactsTable tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));
        const index = {
            'nom': 0,
            'prenom': 1,
            'poste': 3,
            'agence': 4
        }[column];
        const isAscending = this.classList.contains('asc');
        rows.sort((a, b) => {
            const textA = a.cells[index].textContent.toLowerCase();
            const textB = b.cells[index].textContent.toLowerCase();
            return isAscending ?
                textB.localeCompare(textA) :
                textA.localeCompare(textB);
        });
        document.querySelectorAll('.sortable').forEach(h => h.classList.remove('asc', 'desc'));
        this.classList.toggle('asc', !isAscending);
        this.classList.toggle('desc', isAscending);
        rows.forEach(row => tbody.appendChild(row));
    });
});
    document.querySelectorAll('.deleteButton').forEach(function(button) {
    button.addEventListener('click', function (event) {
        if (!confirm('Voulez-vous vraiment supprimer ce contact ?')) {
            event.preventDefault(); // Empêche la navigation si l'utilisateur annule
        }
    });
});
          // Récupération des éléments
        const deleteButton = document.getElementById('deleteButton');
        const modal = document.getElementById('confirmationModal');
        const confirmDelete = document.getElementById('confirmDelete');
        const cancelDelete = document.getElementById('cancelDelete');

        // Afficher la modale lorsque l'utilisateur clique sur "Supprimer"
        deleteButton.addEventListener('click', function () {
            modal.style.display = 'flex';
        });

        // Fermer la modale si l'utilisateur clique sur "Non"
        cancelDelete.addEventListener('click', function () {
            modal.style.display = 'none';
        });

        // Ajouter une action pour le bouton "Oui"
        confirmDelete.addEventListener('click', function () {
            // Redirection ou action de suppression
            alert('Contact supprimé !'); // Remplacez cette ligne par une action réelle
            modal.style.display = 'none';
        });

        // Fermer la modale si l'utilisateur clique en dehors de la boîte
        window.addEventListener('click', function (event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
