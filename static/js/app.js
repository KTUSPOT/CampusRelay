// CampusKit - Client-side Interactive Logic

// --- Toast Notification System ---
function showToast(message, type = 'success', duration = 4000) {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  const bgColors = {
    success: 'bg-emerald-600 text-white',
    error: 'bg-rose-600 text-white',
    warning: 'bg-amber-500 text-white',
    info: 'bg-indigo-600 text-white'
  };

  const icons = {
    success: '<svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>',
    error: '<svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>',
    warning: '<svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>',
    info: '<svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>'
  };

  toast.className = `toast flex items-center p-4 rounded-xl shadow-lg text-sm font-medium ${bgColors[type] || bgColors.info}`;
  toast.innerHTML = `
    ${icons[type] || icons.info}
    <div class="flex-1">${message}</div>
    <button onclick="this.parentElement.remove()" class="ml-3 text-white/80 hover:text-white">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
    </button>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, duration);
}

// --- Demo Account Quick Switcher ---
async function switchDemoUser(role) {
  try {
    const res = await fetch(`/api/demo-login/${role}`, { method: 'POST' });
    const data = await res.json();
    if (data.success) {
      showToast(`Logged in as ${data.user.name} (${data.user.role.toUpperCase()})`, 'success');
      setTimeout(() => {
        if (data.user.role === 'admin') {
          window.location.href = '/admin';
        } else if (data.user.role === 'senior') {
          window.location.href = '/dashboard';
        } else {
          window.location.href = '/marketplace';
        }
      }, 500);
    } else {
      showToast(data.message || 'Failed to switch demo user', 'error');
    }
  } catch (err) {
    showToast('Network error while switching accounts', 'error');
  }
}

// --- WhatsApp Link Formatter ---
function openWhatsAppContact(phone, productName, price, location, sellerName) {
  // Clean phone number
  let cleanPhone = (phone || '').replace(/[^0-9]/g, '');
  if (!cleanPhone.startsWith('91') && cleanPhone.length === 10) {
    cleanPhone = '91' + cleanPhone;
  }
  
  const text = encodeURIComponent(
    `Hi ${sellerName || 'there'}! I saw your listing for "${productName}" (₹${price}) on CampusKit. Is it still available for campus pickup at ${location || 'college'}?`
  );
  
  const waUrl = `https://wa.me/${cleanPhone}?text=${text}`;
  window.open(waUrl, '_blank');
}

// --- Reservation Action ---
async function reserveProduct(productId, sellerPhone, productName, price, location, sellerName) {
  const note = prompt("Add a brief note for the senior (e.g. 'I can meet tomorrow after S1 Graphics lab'):", "Interested in buying! Let's meet on campus.");
  if (note === null) return; // User cancelled prompt

  try {
    const res = await fetch(`/api/products/${productId}/reserve`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ note: note })
    });
    const data = await res.json();
    if (data.success) {
      showToast("Item successfully reserved! 🎉 Opening WhatsApp to contact seller...", "success");
      
      setTimeout(() => {
        openWhatsAppContact(sellerPhone, productName, price, location, sellerName);
        location.reload();
      }, 1200);
    } else {
      showToast(data.message || "Could not reserve item.", "error");
    }
  } catch (err) {
    showToast("Error connecting to server. Please try again.", "error");
  }
}

// --- Update Listing Status ---
async function setProductStatus(productId, newStatus) {
  try {
    const res = await fetch(`/api/products/${productId}/status`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus })
    });
    const data = await res.json();
    if (data.success) {
      showToast(`Listing marked as ${newStatus.toUpperCase()}`, 'success');
      setTimeout(() => window.location.reload(), 600);
    } else {
      showToast(data.message || 'Failed to update status', 'error');
    }
  } catch (err) {
    showToast('Network error updating listing status', 'error');
  }
}

// --- Delete Listing ---
async function deleteListing(productId) {
  if (!confirm("Are you sure you want to permanently delete this listing?")) return;

  try {
    const res = await fetch(`/api/products/${productId}/delete`, {
      method: 'POST'
    });
    const data = await res.json();
    if (data.success) {
      showToast("Listing deleted successfully", "info");
      setTimeout(() => window.location.reload(), 600);
    } else {
      showToast(data.message || "Failed to delete listing", "error");
    }
  } catch (err) {
    showToast("Network error deleting listing", "error");
  }
}

// --- Update Reservation Status (Seller Confirms/Cancels) ---
async function updateReservation(reservationId, newStatus) {
  try {
    const res = await fetch(`/api/reservations/${reservationId}/status`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus })
    });
    const data = await res.json();
    if (data.success) {
      showToast(`Reservation marked as ${newStatus}`, 'success');
      setTimeout(() => window.location.reload(), 600);
    } else {
      showToast(data.message || 'Failed to update reservation', 'error');
    }
  } catch (err) {
    showToast('Network error updating reservation', 'error');
  }
}

// --- Live Savings Calculator for Sell Form ---
function calculateFormSavings() {
  const origInput = document.getElementById('original_price');
  const sellInput = document.getElementById('price');
  const previewBox = document.getElementById('savings-preview-box');
  const savingsText = document.getElementById('savings-text');
  const percentText = document.getElementById('savings-percent');

  if (!origInput || !sellInput || !previewBox) return;

  const original = parseFloat(origInput.value) || 0;
  const selling = parseFloat(sellInput.value) || 0;

  if (original > 0 && selling > 0 && original > selling) {
    const savings = original - selling;
    const percent = Math.round((savings / original) * 100);
    previewBox.classList.remove('hidden');
    if (savingsText) savingsText.innerText = `₹${savings.toLocaleString('en-IN')}`;
    if (percentText) percentText.innerText = `${percent}%`;
  } else {
    if (previewBox) previewBox.classList.add('hidden');
  }
}

// Mobile Nav Toggle
document.addEventListener('DOMContentLoaded', () => {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
  }
});
