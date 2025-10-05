import express from 'express';
import { uploadCampaignImage, uploadProfileImage, uploadGeneral, deleteFromCloudinary } from '../config/cloudinary.js';
import { authenticateToken } from '../middleware/auth.js';

const router = express.Router();

// Upload campaign image
router.post('/campaign-image', authenticateToken, (req, res) => {
  uploadCampaignImage.single('image')(req, res, (error) => {
    if (error) {
      return res.status(400).json({
        success: false,
        message: error.message || 'Error uploading campaign image',
      });
    }

    if (!req.file) {
      return res.status(400).json({
        success: false,
        message: 'No image file provided',
      });
    }

    res.json({
      success: true,
      message: 'Campaign image uploaded successfully',
      imageUrl: req.file.path,
      publicId: req.file.filename,
      originalName: req.file.originalname,
    });
  });
});

// Upload profile image
router.post('/profile-image', authenticateToken, (req, res) => {
  uploadProfileImage.single('profileImage')(req, res, (error) => {
    if (error) {
      return res.status(400).json({
        success: false,
        message: error.message || 'Error uploading profile image',
      });
    }

    if (!req.file) {
      return res.status(400).json({
        success: false,
        message: 'No image file provided',
      });
    }

    res.json({
      success: true,
      message: 'Profile image uploaded successfully',
      imageUrl: req.file.path,
      publicId: req.file.filename,
      originalName: req.file.originalname,
    });
  });
});

// Upload general file
router.post('/general', authenticateToken, (req, res) => {
  uploadGeneral.single('file')(req, res, (error) => {
    if (error) {
      return res.status(400).json({
        success: false,
        message: error.message || 'Error uploading file',
      });
    }

    if (!req.file) {
      return res.status(400).json({
        success: false,
        message: 'No file provided',
      });
    }

    res.json({
      success: true,
      message: 'File uploaded successfully',
      fileUrl: req.file.path,
      publicId: req.file.filename,
      originalName: req.file.originalname,
      fileType: req.file.mimetype,
      fileSize: req.file.size,
    });
  });
});

// Upload multiple images
router.post('/multiple-images', authenticateToken, (req, res) => {
  uploadGeneral.array('images', 5)(req, res, (error) => {
    if (error) {
      return res.status(400).json({
        success: false,
        message: error.message || 'Error uploading images',
      });
    }

    if (!req.files || req.files.length === 0) {
      return res.status(400).json({
        success: false,
        message: 'No image files provided',
      });
    }

    const uploadedFiles = req.files.map(file => ({
      imageUrl: file.path,
      publicId: file.filename,
      originalName: file.originalname,
    }));

    res.json({
      success: true,
      message: `${req.files.length} images uploaded successfully`,
      files: uploadedFiles,
    });
  });
});

// Delete file from Cloudinary
router.delete('/delete/:publicId', authenticateToken, async (req, res) => {
  try {
    const { publicId } = req.params;
    
    if (!publicId) {
      return res.status(400).json({
        success: false,
        message: 'Public ID is required',
      });
    }

    // Decode the publicId (it might be URL encoded)
    const decodedPublicId = decodeURIComponent(publicId);
    
    const result = await deleteFromCloudinary(decodedPublicId);
    
    if (result.result === 'ok') {
      res.json({
        success: true,
        message: 'File deleted successfully',
        result,
      });
    } else {
      res.status(400).json({
        success: false,
        message: 'Failed to delete file',
        result,
      });
    }
  } catch (error) {
    console.error('Delete file error:', error);
    res.status(500).json({
      success: false,
      message: 'Error deleting file',
      error: error.message,
    });
  }
});

// Get upload statistics (admin only)
router.get('/stats', authenticateToken, async (req, res) => {
  try {
    // This would typically fetch from database or Cloudinary API
    const mockStats = {
      totalUploads: 156,
      totalSize: '245.7 MB',
      campaignImages: 89,
      profileImages: 45,
      generalFiles: 22,
      storageUsed: '62%',
      recentUploads: [
        {
          filename: 'campaign-image-1.jpg',
          uploadedBy: 'John Doe',
          uploadedAt: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
          size: '2.4 MB',
          type: 'Campaign Image'
        },
        {
          filename: 'profile-pic.png',
          uploadedBy: 'Jane Smith',
          uploadedAt: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(),
          size: '1.1 MB',
          type: 'Profile Image'
        }
      ]
    };

    res.json({
      success: true,
      stats: mockStats,
    });
  } catch (error) {
    console.error('Get upload stats error:', error);
    res.status(500).json({
      success: false,
      message: 'Error fetching upload statistics',
    });
  }
});

// Health check for upload service
router.get('/health', (req, res) => {
  res.json({
    success: true,
    message: 'Upload service is healthy',
    timestamp: new Date().toISOString(),
    services: {
      cloudinary: 'connected',
      multer: 'active',
    },
  });
});

export default router;
