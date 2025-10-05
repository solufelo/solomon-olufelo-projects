export interface UserTypeProps {
  id: string;
  name: string;
  email: string;
  role: string;
  createdAt: string;
  updatedAt: string;
}

export interface Campaign {
  _id?: string;
  title: string;
  description: string;
  organizer: string;
  image: string;
  EventTargetAmount: number;
  EventCurrentAmount: number;
  createdAt?: Date;
  updatedAt?: Date;
  status: string;
  EventCategory: string;
  location: string;
  endDate: Date;
  isActive?: boolean;
  isDeleted?: boolean;
  isFeatured?: boolean;
  isApproved?: boolean;
  isRejected?: boolean;
  isArchived?: boolean;
}

export interface Donation {
  _id?: string;
  campaignId: string;
  campaignTitle: string;
  donorId: string;
  donorName: string;
  donorEmail: string;
  amount: number;
  message?: string;
  isAnonymous: boolean;
  paymentMethod: "credit_card" | "paypal" | "bank_transfer" | "crypto";
  paymentStatus: "pending" | "completed" | "failed" | "refunded";
  transactionId?: string;
  receiptUrl?: string;
  createdAt?: Date;
  updatedAt?: Date;
  refundReason?: string;
  processingFee: number;
  netAmount: number;
}

export interface PaymentIntent {
  id: string;
  amount: number;
  currency: string;
  status:
    | "requires_payment_method"
    | "requires_confirmation"
    | "requires_action"
    | "processing"
    | "requires_capture"
    | "canceled"
    | "succeeded";
  clientSecret: string;
}
