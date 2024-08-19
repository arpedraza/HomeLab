terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = "~> 2.9"
    }
  }
}

provider "proxmox" {
  pm_api_url      = "https://192.168.1.55:8006/api2/json"
  pm_user         = "tfsvc@192.168.1.55"
  pm_password     = "99243775-caef-4e30-b4a0-217234ab44b4"
  pm_tls_insecure = true
}

# Define the first VM
resource "proxmox_vm_qemu" "k3s-n1" {
  name        = "k3s-n1"
  target_node = "pve1"

  # Disk configuration
  disk {
    type      = "scsi"        # Disk type
    storage   = "local-lvm"   # Storage location
    size      = "40G"         # Disk size
  }

  # CPU and memory configuration
  cores   = 1
  memory  = 2048

  # Network configuration
  network {
    model  = "virtio"        # Network interface model
    bridge = "vmbr0"         # Bridge to connect the VM to
  }

  # Operating system setup using the latest Ubuntu server ISO
  clone     = "ubuntu-22.04-template"  
  os_type   = "cloud-init"             # Use 'cloud-init' for modern Ubuntu server images
  boot      = "cdn"
  bootdisk  = "scsi0"
  scsihw    = "virtio-scsi-pci"
  agent     = 1                        # Enable QEMU guest agent
}

# Define the second VM
resource "proxmox_vm_qemu" "k3s-n2" {
  name        = "k3s-n2"
  target_node = "pve1"

  # Disk configuration
  disk {
    type      = "scsi"        # Disk type
    storage   = "local-lvm"   # Storage location
    size      = "20G"         # Disk size
  }

  # CPU and memory configuration
  cores   = 2
  memory  = 2048

  # Network configuration
  network {
    model  = "virtio"        # Network interface model
    bridge = "vmbr0"         # Bridge to connect the VM to
  }

  # Operating system setup using the latest Ubuntu server ISO
  clone     = "ubuntu-22.04-template"  
  os_type   = "cloud-init"             # Use 'cloud-init' for modern Ubuntu server images
  boot      = "cdn"
  bootdisk  = "scsi0"
  scsihw    = "virtio-scsi-pci"
  agent     = 1                        # Enable QEMU guest agent
}